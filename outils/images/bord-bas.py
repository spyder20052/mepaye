"""Nettoie le bas d'un téléphone détouré (hero). Le contour du bas est modélisé comme celui d'un vrai iPhone :
bords gauche et droit (droites mesurées sur l'image), bord inférieur (droite ajustée sur le dernier pixel de
titane clair de la partie plate), coins en arcs de cercle tangents. Tout ce qui dépasse ce contour
(bande d'ombre sombre, ergots, halo) est retiré, avec un anticrénelage d'un pixel ; rien n'est ajouté.
Usage : python3 bord-bas.py source.webp sortie.webp [R_gauche] [R_droit]"""
import sys, numpy as np
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
R = float(sys.argv[3]) if len(sys.argv) > 3 else 150      # coin gauche
R2 = float(sys.argv[4]) if len(sys.argv) > 4 else 70     # coin droit, plus serré dans la perspective
im = np.asarray(Image.open(src).convert('RGBA')).astype(np.float32)
h, w = im.shape[:2]; a = im[..., 3]; L = im[..., :3].mean(2)
m = a > 128
# bords latéraux : x = p*y + q, mesurés sur une portion droite
ys = np.arange(h - 700, h - 260)
pl, ql = np.polyfit(ys, [np.argmax(m[y]) for y in ys], 1)
pr, qr = np.polyfit(ys, [w - 1 - np.argmax(m[y][::-1]) for y in ys], 1)
# bord inférieur : y = r*x + s, sur le dernier pixel de titane clair au centre
zone = 140; y0 = h - zone
bx = np.arange(int(w * .2), int(w * .8)); yb = []
for x in bx:
    ok = np.nonzero((a[y0:, x] > 180) & (L[y0:, x] > 95))[0]; yb.append(y0 + ok.max() if len(ok) else np.nan)
yb = np.array(yb); g = ~np.isnan(yb)
r, s = np.polyfit(bx[g], yb[g], 1)
for _ in range(3):                                   # robustesse : on écarte les ergots
    res = yb[g] - (r * bx[g] + s); keep = np.abs(res) < max(1.5, 2 * res.std()); r, s = np.polyfit(bx[g][keep], yb[g][keep], 1)
yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
nb = np.hypot(1, r)
d_bot = ((r * xx + s + .5) - yy) / nb                # > 0 au-dessus du bord inférieur
d_l = (xx - (pl * yy + ql)) / np.hypot(1, pl)        # > 0 à droite du bord gauche
d_r = ((pr * yy + qr) - xx) / np.hypot(1, pr)        # > 0 à gauche du bord droit
def corner(dside, cx_guess, sign):
    # centre de l'arc : à R du bord latéral et du bord inférieur
    from scipy.optimize import fsolve
    if sign < 0: f = lambda c: [(c[0] - (pl * c[1] + ql)) / np.hypot(1, pl) - R, ((r * c[0] + s + .5) - c[1]) / nb - R]
    else:        f = lambda c: [((pr * c[1] + qr) - c[0]) / np.hypot(1, pr) - R2, ((r * c[0] + s + .5) - c[1]) / nb - R2]
    return fsolve(f, [cx_guess, h - (R if sign < 0 else R2)])
clx, cly = corner(d_l, ql + R, -1); crx, cry = corner(d_r, qr - R, 1)
dist = np.minimum(np.minimum(d_bot, d_l), d_r)
inl = (xx < clx) & (yy > cly); inr = (xx > crx) & (yy > cry)
dist = np.where(inl, R - np.hypot(xx - clx, yy - cly), dist)
dist = np.where(inr, R2 - np.hypot(xx - crx, yy - cry), dist)
shape = np.clip(dist + .5, 0, 1)
shape[:h - 260] = 1                                   # on ne touche qu'au bas
out = im.copy(); out[..., 3] = np.minimum(a, shape * 255)
Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(dst, 'WEBP', quality=92, method=6, exact=True)
print('gauche x=%.4fy+%.1f droite x=%.4fy+%.1f bas y=%.4fx+%.1f arcs (%.0f,%.0f) (%.0f,%.0f)' % (pl, ql, pr, qr, r, s, clx, cly, crx, cry))
