import sys
from PIL import Image
S, SITE = sys.argv[1], sys.argv[2]
D = S + '/dl-pexels'
def crop(src, fx, fy, fw, ratio, out, size, mode='RGB', q=86):
    im = Image.open(src).convert(mode)
    W, H = im.size
    w = fw * W; h = w / ratio
    x0, y0 = fx * W, fy * H
    if y0 + h > H: y0 = H - h
    box = tuple(round(v) for v in (x0, y0, x0 + w, y0 + h))
    im.crop(box).resize(size, Image.LANCZOS).save(out, 'WEBP', quality=q, method=6)
    print(out.split('/')[-1], box, size)
# créatrice détourée, même proportion que l'ancienne (941 × 1192)
crop(S + '/cut/A-cut.png', 0.0, 0.13, 0.95, 941 / 1192, SITE + '/assets/img/creatrice.webp', (1176, 1490), 'RGBA', 88)
crop(D + '/B-25752284.jpg', 0.10, 0.05, 0.80, 4 / 5, SITE + '/assets/img/usage-abidjan.webp', (960, 1200))
crop(D + '/C-21414936.jpg', 0.07, 0.15, 0.86, 4 / 5, SITE + '/assets/img/usage-cotonou.webp', (960, 1200))
crop(D + '/D-7229076.jpg', 0.0, 0.12, 1.0, 4 / 5, SITE + '/assets/img/usage-dakar.webp', (960, 1200))
crop(D + '/E-6787048.jpg', 0.22, 0.0, 0.5625, 1, SITE + '/assets/img/mains.webp', (1200, 1200))
