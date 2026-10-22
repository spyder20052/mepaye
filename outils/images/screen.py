import sys
import numpy as np
from PIL import Image
from collections import deque
im = np.asarray(Image.open(sys.argv[1]).convert('RGB')).astype(int)
h, w, _ = im.shape
white = (im.min(2) > 238) & (np.abs(im[..., 0] - im[..., 2]) < 14)
# plus grande zone blanche reliée
seen = np.zeros_like(white); best = []
step = 4
for y in range(0, h, step):
    for x in range(0, w, step):
        if white[y, x] and not seen[y, x]:
            q = deque([(y, x)]); seen[y, x] = 1; comp = []
            while q:
                cy, cx = q.popleft(); comp.append((cy, cx))
                for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                    ny, nx = cy+dy, cx+dx
                    if 0 <= ny < h and 0 <= nx < w and white[ny, nx] and not seen[ny, nx]:
                        seen[ny, nx] = 1; q.append((ny, nx))
            if len(comp) > len(best): best = comp
pts = np.array(best)  # (y, x)
s = pts[:, 0] + pts[:, 1]; d = pts[:, 1] - pts[:, 0]
tl = pts[s.argmin()]; br = pts[s.argmax()]; tr = pts[d.argmax()]; bl = pts[d.argmin()]
print('pixels', len(best))
for n, p in [('tl', tl), ('tr', tr), ('br', br), ('bl', bl)]: print(n, int(p[1]), int(p[0]))
mask = np.zeros((h, w), np.uint8); mask[pts[:, 0], pts[:, 1]] = 255
Image.fromarray(mask).save(sys.argv[2])
