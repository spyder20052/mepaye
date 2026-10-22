"""Détourage sur fond blanc uni.
- Les surfaces blanches du sujet (chaussures, t-shirt) gardent le contour net de macOS.
- Près des cheveux et des zones sombres, la transparence vient de l'écart au blanc :
  les trous de fond coincés entre les tresses deviennent transparents.
- Les pixels de bord sont « démélangés » du blanc : aucun liseré clair, aucun halo flou."""
import sys
import numpy as np
from PIL import Image, ImageFilter
src, vis, out = sys.argv[1:4]
img = Image.open(src).convert('RGB'); C = np.asarray(img).astype(np.float32)
V = Image.open(vis).getchannel('A')
Va = np.asarray(V).astype(np.float32) / 255
mn = C.min(2)
# 1. transparence physique d'un cheveu noir sur fond blanc : a = (blanc - pixel) / (blanc - noir)
K = np.clip((251 - mn) / 210, 0, 1)
# 2. zone des cheveux : à moins de 4 px d'un pixel très sombre (tresses), seulement si demandé
hair_on = len(sys.argv) > 4 and sys.argv[4] == 'hair'
hair = np.asarray(Image.fromarray(((mn < 60) * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(9))) > 0
# 3. bande de bord (à moins de 14 px à l'intérieur du contour macOS)
core = np.asarray(V.point(lambda v: 255 if v > 128 else 0).filter(ImageFilter.MinFilter(29))) > 0
band = (Va > 0.02) & ~core
# alpha : contour macOS resserré d'1 px partout ; dans les cheveux du bord, la clé physique
Vt = np.asarray(V.filter(ImageFilter.MinFilter(3))).astype(np.float32) / 255
A = Vt.copy()
if hair_on:
    sel = band & hair
    A[sel] = np.minimum(K[sel], np.clip(Va[sel] * 3, 0, 1))
    # le fond pur (blanc neutre) coincé un peu plus loin entre les mèches : transparent aussi
    wide = np.asarray(Image.fromarray(((mn < 60) * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(19))) > 0
    sat = C.max(2) - mn
    trapped = band & wide & (mn >= 247) & (sat <= 3)
    A[trapped] = 0
A = np.where(core, 1.0, A)
if hair_on:
    # à l'intérieur aussi : le blanc pur du studio (254) entre deux mèches ; le t-shirt crème reste plein
    inner = (Va > 0.02) & wide & (mn >= 250) & (sat <= 2)
    soft = np.clip((mn - 246) / 6, 0, 1)
    A = np.where(inner, np.minimum(A, 1 - soft), A)
# léger lissage sub-pixel, sans flou visible
A = np.asarray(Image.fromarray((A * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.45))).astype(np.float32) / 255
A[A < .03] = 0
# 4. démélange du blanc : F = (C - (1 - a) * 255) / a
B = 250.0
F = (C - (1 - A[..., None]) * B) / np.maximum(A[..., None], .06)
F = np.where(A[..., None] > .985, C, F).clip(0, 255)
Image.fromarray(np.dstack([F, A * 255]).astype(np.uint8), 'RGBA').save(out)
print('ok')
