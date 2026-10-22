"""Pose chaque portrait détouré sur le même fond de studio mepaye :
papier bleu pâle, lumière douce venue de la gauche, grande arche blanche, ombre portée légère."""
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageChops
S, OUT = sys.argv[1], sys.argv[2]
W, H = 960, 1200

def backdrop():
    bg = Image.new('RGB', (W, H))
    top, bot = (231, 239, 255), (203, 221, 251)
    d = ImageDraw.Draw(bg)
    for y in range(H):
        t = y / (H - 1)
        d.line([(0, y), (W, y)], fill=tuple(round(top[i] + (bot[i] - top[i]) * t) for i in range(3)))
    # lumière douce, venue d'en haut à gauche
    glow = Image.new('L', (W, H), 0)
    ImageDraw.Draw(glow).ellipse((-W * .25, -H * .2, W * .85, H * .62), fill=150)
    glow = glow.filter(ImageFilter.GaussianBlur(160))
    bg = Image.composite(Image.new('RGB', (W, H), (255, 255, 255)), bg, glow)
    # l'arche mepaye, entière, posée sur le bord bas
    aw, ah = int(W * .74), int(H * .8)
    ax, ay = (W - aw) // 2, H - ah
    arch = Image.new('L', (W, H), 0)
    da = ImageDraw.Draw(arch)
    da.ellipse((ax, ay, ax + aw, ay + aw), fill=255)
    da.rectangle((ax, ay + aw // 2, ax + aw, H), fill=255)
    arch_soft = arch.filter(ImageFilter.GaussianBlur(1.2)).point(lambda v: v * .78)
    bg = Image.composite(Image.new('RGB', (W, H), (250, 252, 255)), bg, arch_soft)
    # liseré de l'arche
    edge = ImageChops.subtract(arch, arch.filter(ImageFilter.MinFilter(5))).filter(ImageFilter.GaussianBlur(.8)).point(lambda v: v * .35)
    bg = Image.composite(Image.new('RGB', (W, H), (255, 255, 255)), bg, edge)
    return bg

def person(path, head_top=.22, head_x=.5):
    im = Image.open(path).convert('RGBA')
    # bords nets : on resserre l'alpha d'un pixel pour retirer le liseré de l'ancien fond
    a = im.getchannel('A').filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(.7))
    im.putalpha(a)
    # étalonnage commun : un peu moins saturé, un peu plus de contraste, une pointe de froid
    rgb = im.convert('RGB')
    rgb = ImageEnhance.Color(rgb).enhance(.9)
    rgb = ImageEnhance.Contrast(rgb).enhance(1.05)
    r, g, b = rgb.split()
    rgb = Image.merge('RGB', (r.point(lambda v: v * .985), g, b.point(lambda v: min(255, v * 1.02 + 2))))
    im = Image.merge('RGBA', (*rgb.split(), a))
    bx = a.getbbox()
    # la tête : la bande haute de la silhouette
    head = a.crop((0, bx[1], im.width, bx[1] + int((bx[3] - bx[1]) * .12))).getbbox()
    hx = (head[0] + head[2]) / 2 if head else im.width / 2
    s = (H * (1 - head_top)) / (im.height - bx[1])
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    px = round(W * head_x - hx * s); py = round(H * head_top - bx[1] * s)
    return im, px, py

def compose(name, out, **kw):
    bg = backdrop().convert('RGBA')
    im, px, py = person(f'{S}/cut/{name}-cut.png', **kw)
    # ombre portée douce, décalée vers la droite comme la lumière vient de gauche
    sh = Image.new('RGBA', bg.size, (0, 0, 0, 0))
    alpha = Image.new('L', bg.size, 0); alpha.paste(im.getchannel('A'), (px + 26, py + 18))
    alpha = alpha.filter(ImageFilter.GaussianBlur(28)).point(lambda v: v * .22)
    sh.putalpha(alpha); sh = Image.composite(Image.new('RGBA', bg.size, (16, 36, 74, 255)), sh, alpha)
    bg.alpha_composite(sh)
    layer = Image.new('RGBA', bg.size, (0, 0, 0, 0)); layer.paste(im, (px, py), im)
    bg.alpha_composite(layer)
    bg.convert('RGB').save(out, 'WEBP', quality=88, method=6)
    print('ok', out.split('/')[-1])

compose('B-25752284', f'{OUT}/usage-abidjan.webp', head_top=.2, head_x=.47)
compose('C-21414936', f'{OUT}/usage-cotonou.webp', head_top=.2, head_x=.5)
compose('D-7229076', f'{OUT}/usage-dakar.webp', head_top=.2, head_x=.43)
