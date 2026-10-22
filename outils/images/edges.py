import sys, json
import numpy as np
from PIL import Image, ImageFilter
C = sys.argv[1]
m = Image.open(C + '/screen-mask.png').convert('L')
M = np.asarray(m) > 128
E = M & ~(np.asarray(m.filter(ImageFilter.MinFilter(3))) > 128)
ys, xs = np.nonzero(E); B = np.stack([xs, ys], 1).astype(float)
q = np.array(json.load(open(C + '/quad.json'))['quad'])
lines = []
spans = {0: [(.1, .3), (.7, .9)], 1: [(.15, .85)], 2: [(.15, .85)], 3: [(.15, .85)]}
for i in range(4):
    a, b = q[i], q[(i + 1) % 4]; d = b - a; L = np.hypot(*d); u = d / L; n = np.array([-u[1], u[0]])
    t = (B - a) @ u / L; off = (B - a) @ n
    sel = (np.abs(off) < 25) & np.any([(t > lo) & (t < hi) for lo, hi in spans[i]], 0)
    P = B[sel]; c = P.mean(0); _, _, Vt = np.linalg.svd(P - c)
    lines.append((c, Vt[0]))
def inter(l1, l2):
    (p, r), (q2, s) = l1, l2
    A = np.array([r, -s]).T; t = np.linalg.solve(A, q2 - p); return (p + t[0] * r).tolist()
corners = [inter(lines[3], lines[0]), inter(lines[0], lines[1]), inter(lines[1], lines[2]), inter(lines[2], lines[3])]
json.dump({'quad': corners}, open(C + '/quad2.json', 'w'))
print(json.dumps([[round(v, 1) for v in c] for c in corners]))
