import sys, json
import numpy as np
from PIL import Image, ImageFilter, ImageChops
S, SITE = sys.argv[1], sys.argv[2]
C = S + '/camp'
base = Image.open(C + '/mains.webp').convert('RGB'); W, H = base.size
ui = Image.open(C + '/screen.png').convert('RGB'); uw, uh = ui.size
q = json.load(open(C + '/quad2.json'))['quad']
# coefficients de perspective : pour chaque pixel de destination, le pixel source dans l'écran
def coeffs(dst, src):
    A = []; B = []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; B += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(B, float)).tolist()
src = [(0, 0), (uw, 0), (uw, uh), (0, uh)]
warped = ui.transform((W, H), Image.PERSPECTIVE, coeffs(q, src), Image.BICUBIC)
cover = Image.new('L', (uw, uh), 255).transform((W, H), Image.PERSPECTIVE, coeffs(q, src), Image.BICUBIC)
# l'écran réel : la zone blanche détectée, adoucie d'un pixel ; on n'écrit jamais hors du verre
m = Image.open(C + '/screen-mask.png').convert('L').filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
mask = ImageChops.multiply(m, cover)
# un léger reflet de verre, du haut gauche vers le bas, pour que l'écran appartienne à la photo
g = Image.linear_gradient('L').rotate(25, expand=False).resize((W, H)).point(lambda v: int(max(0, 60 - v * .5)))
glare = Image.composite(Image.new('RGB', (W, H), (255, 255, 255)), warped, g.point(lambda v: v * .35))
out = Image.composite(glare, base, mask)
out.save(SITE + '/assets/img/mains.webp', 'WEBP', quality=90, method=6)
out.crop((450, 100, 1100, 900)).save(C + '/mains-zoom.png')
print('ok', W, H)
