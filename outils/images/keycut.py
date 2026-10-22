"""Détourage sur fond de studio uni : la transparence vient de l'écart à la couleur du fond
(mesurée localement), la couleur du bord est « démélangée » du fond. Le masque de macOS
ne sert qu'à borner la zone du sujet."""
import sys
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
src, vis, out = sys.argv[1:4]
img = Image.open(src).convert('RGB'); W, H = img.size
C = np.asarray(img).astype(np.float32)
V = Image.open(vis).getchannel('A')
# 1. plaque de fond : moyenne locale des pixels de fond, prolongée sous le sujet
bgm = np.asarray(V.filter(ImageFilter.MaxFilter(31))) < 8
k = 4; small = (W // k, H // k)
wgt = Image.fromarray((bgm * 255).astype(np.uint8)).resize(small, Image.BILINEAR)
plate = []
for r in (6, 18, 50):
    wb = np.asarray(wgt.filter(ImageFilter.GaussianBlur(r))).astype(np.float32) / 255
    chans = [np.asarray(Image.fromarray((C[..., c] * bgm).astype(np.uint8)).resize(small, Image.BILINEAR).filter(ImageFilter.GaussianBlur(r))).astype(np.float32) for c in range(3)]
    plate.append((np.stack(chans, -1), wb))
B = np.zeros((small[1], small[0], 3), np.float32); have = np.zeros((small[1], small[0]), bool)
for est, wb in plate:
    ok = (wb > .05) & ~have
    B[ok] = est[ok] / wb[ok, None]; have |= ok
B[~have] = C[bgm].mean(0)
B = np.stack([np.asarray(Image.fromarray(B[..., c].clip(0, 255).astype(np.uint8)).resize((W, H), Image.BICUBIC)).astype(np.float32) for c in range(3)], -1)
# 2. transparence : écart à la plaque, pondéré vers le bleu (le fond est bleuté, la peau et le t-shirt ne le sont pas)
D = C - B
d = np.sqrt((D[..., 0] * 1.2) ** 2 + D[..., 1] ** 2 + (D[..., 2] * 1.4) ** 2)
A = np.clip((d - 13) / (34 - 13), 0, 1)
# bornes : rien hors du sujet élargi ; tout opaque dans le visage (yeux, dents)
Vd = np.asarray(V.filter(ImageFilter.MaxFilter(25))).astype(np.float32) / 255
A *= Vd
face = Image.new('L', (W, H), 0); ImageDraw.Draw(face).ellipse((650 - 108, 262 - 118, 650 + 108, 262 + 118), fill=255)
face = np.asarray(face.filter(ImageFilter.GaussianBlur(10))).astype(np.float32) / 255
A = np.maximum(A, face * (np.asarray(V).astype(np.float32) / 255))
# l'intérieur du sujet (trous du masque bouchés, à plus de 30 px du contour) reste plein :
# les reflets du t-shirt blanc ne deviennent pas transparents
vb = V.point(lambda v: 255 if v > 128 else 0)
filled = vb.copy(); ImageDraw.floodfill(filled, (0, 0), 128)
inside = np.asarray(filled) != 128
inner = Image.fromarray((inside * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(61)).filter(ImageFilter.GaussianBlur(6))
# … sauf là où le pixel est le fond lui-même (trous entre les tresses)
notbg = np.clip((d - 9) / 8, 0, 1)
A = np.maximum(A, np.asarray(inner).astype(np.float32) / 255 * notbg)
# le t-shirt blanc (sous les épaules, à droite de la main) : le contour de macOS, net sur un bord blanc
shirt = Image.new('L', (W, H), 0); dr = ImageDraw.Draw(shirt); dr.rectangle((330, 410, W, H), fill=255); dr.rectangle((235, 545, W, H), fill=255)
shirt = np.asarray(shirt.filter(ImageFilter.GaussianBlur(14))).astype(np.float32) / 255
Vs = np.asarray(V.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(.8))).astype(np.float32) / 255
lum = C @ np.array([.3, .59, .11], np.float32)
A = np.maximum(A, shirt * Vs * (lum > 150))
# lissage léger, sans effet d'escalier
A = np.asarray(Image.fromarray((A * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.6))).astype(np.float32) / 255
# 3. démélange : F = B + (C - B) / alpha, la couleur du bord ne garde rien du fond
F = B + (C - B) / np.maximum(A, .08)[..., None]
F = np.where(A[..., None] > .97, C, F).clip(0, 255)
Image.fromarray(np.dstack([F, A * 255]).astype(np.uint8)).save(out)
print('ok')
