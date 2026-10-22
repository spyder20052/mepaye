import sys, json
import numpy as np
from PIL import Image
m = np.asarray(Image.open(sys.argv[1]))
ys, xs = np.nonzero(m); P = np.stack([xs, ys], 1).astype(float)
c = P.mean(0); U, Sg, Vt = np.linalg.svd(P - c, full_matrices=False)
ax = Vt  # ax[0] = long axis
proj = (P - c) @ ax.T
lo, hi = np.percentile(proj, .3, 0), np.percentile(proj, 99.7, 0)
corners = []
for a, b in [(lo[0], lo[1]), (lo[0], hi[1]), (hi[0], hi[1]), (hi[0], lo[1])]:
    corners.append((c + a * ax[0] + b * ax[1]).tolist())
# ordonne : haut-gauche, haut-droite, bas-droite, bas-gauche
corners = sorted(corners, key=lambda p: p[1])
top = sorted(corners[:2], key=lambda p: p[0]); bot = sorted(corners[2:], key=lambda p: p[0])
q = [top[0], top[1], bot[1], bot[0]]
wv = np.hypot(*np.subtract(q[1], q[0])); hv = np.hypot(*np.subtract(q[3], q[0]))
print(json.dumps({'quad': q, 'w': wv, 'h': hv, 'ratio': hv / wv, 'angle': float(np.degrees(np.arctan2(q[1][1]-q[0][1], q[1][0]-q[0][0])))}))
