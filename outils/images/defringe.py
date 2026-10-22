"""Détourage propre : masque resserré, bords adoucis, et couleurs du bord reprises au sujet
(le fond clair d'origine ne déborde plus en liseré)."""
import sys
import numpy as np
from PIL import Image, ImageFilter
src, cut, out = sys.argv[1], sys.argv[2], sys.argv[3]
rgb = np.asarray(Image.open(src).convert('RGB')).astype(np.float32)
a0 = Image.open(cut).convert('RGBA').getchannel('A')
# 1. masque : on retire 2 px de bord puis on adoucit d'1 px
a = a0.filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(1.1))
A = np.asarray(a).astype(np.float32) / 255
# 2. couleur : seuls les pixels bien à l'intérieur gardent leur couleur ; le bord reçoit la moyenne
#    des pixels intérieurs voisins (convolution normalisée), donc plus aucune trace du fond
core = (np.asarray(a0.filter(ImageFilter.MinFilter(9))) > 250).astype(np.float32)
fill = rgb.copy()
for r in (3, 6, 12, 24):
    w = np.asarray(Image.fromarray((core * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(r))).astype(np.float32) / 255
    acc = np.stack([np.asarray(Image.fromarray((rgb[..., c] * core).astype(np.uint8)).filter(ImageFilter.GaussianBlur(r))).astype(np.float32) for c in range(3)], -1)
    est = acc / np.maximum(w[..., None], 1e-3)
    need = (core < 1) & (w > .02)
    fill[need] = est[need]
    core = np.maximum(core, (w > .02).astype(np.float32) * 0)  # on garde le noyau d'origine
# mélange : intérieur = couleur réelle, bord = couleur reprise
inner = (np.asarray(a0.filter(ImageFilter.MinFilter(9))) > 250)[..., None]
col = np.where(inner, rgb, fill)
img = np.dstack([col.clip(0, 255), A * 255]).astype(np.uint8)
Image.fromarray(img, 'RGBA').save(out)
print('ok')
