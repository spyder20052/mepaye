"""Les pixels du bord prennent la couleur du sujet le plus proche (jamais celle du fond),
et le contour est resserré d'un cran : plus aucun liseré clair."""
import sys
import numpy as np
from PIL import Image, ImageFilter
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGBA'); C = np.asarray(im).astype(np.float32)
A = C[..., 3] / 255; rgb = C[..., :3]
# resserrage : les bords à moins de 20 % d'opacité disparaissent, le reste est étiré
A2 = np.clip((A - .2) / .75, 0, 1) ** 1.15
solid = (A > .96).astype(np.float32)
col = rgb.copy(); done = solid > 0
for r in (1.5, 3, 6, 12, 24):
    w = np.asarray(Image.fromarray((solid * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(r))).astype(np.float32) / 255
    acc = np.stack([np.asarray(Image.fromarray((rgb[..., c] * solid).clip(0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(r))).astype(np.float32) for c in range(3)], -1)
    est = acc / np.maximum(w[..., None], 1e-4)
    new = (~done) & (w > .03)
    col[new] = est[new]; done |= new
Image.fromarray(np.dstack([col, A2 * 255]).clip(0, 255).astype(np.uint8)).save(out)
