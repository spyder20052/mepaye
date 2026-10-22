"""Incruste un écran de l'app dans le vert chroma d'une photo : coins retrouvés par
ajustement des quatre bords, perspective, doigts gardés devant, liseré vert supprimé."""
import sys, json, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from collections import deque

def green_alpha(C):
    r, g, b = C[..., 0], C[..., 1], C[..., 2]
    k = g - np.maximum(r, b)
    return np.clip((k - 62) / 58, 0, 1)

def largest(mask):
    h, w = mask.shape; lab = np.zeros((h, w), np.int32); best, bl, cur = 0, 0, 0
    for y in range(0, h, 3):
        for x in range(0, w, 3):
            if mask[y, x] and not lab[y, x]:
                cur += 1; q = deque([(y, x)]); lab[y, x] = cur; n = 0
                while q:
                    cy, cx = q.popleft(); n += 1
                    for ny, nx in ((cy+1,cx),(cy-1,cx),(cy,cx+1),(cy,cx-1)):
                        if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not lab[ny, nx]:
                            lab[ny, nx] = cur; q.append((ny, nx))
                if n > best: best, bl = n, cur
    return lab == bl

def fit_quad(m):
    # contour du masque bouché (les doigts ne déforment pas les bords)
    ys, xs = np.nonzero(m)
    pts = np.stack([xs, ys], 1).astype(float)
    s = pts.sum(1); d = pts[:, 0] - pts[:, 1]
    tl, br, tr, bl = pts[s.argmin()], pts[s.argmax()], pts[d.argmax()], pts[d.argmin()]
    edge = m & ~np.asarray(Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3))).astype(bool)
    ey, ex = np.nonzero(edge); E = np.stack([ex, ey], 1).astype(float)
    lines = []
    for A, B in ((tl, tr), (tr, br), (br, bl), (bl, tl)):
        v = B - A; L = np.linalg.norm(v); u = v / L; nrm = np.array([-u[1], u[0]])
        t = (E - A) @ u / L; dist = np.abs((E - A) @ nrm)
        sel = E[(t > .03) & (t < .97) & (dist < 0.08 * L)]
        # RANSAC : la droite qui aligne le plus de points du bord (les doigts posés dessus sont écartés)
        rng = np.random.default_rng(7); best, bi = None, -1
        for _ in range(400):
            i, j = rng.choice(len(sel), 2, replace=False)
            p, q2 = sel[i], sel[j]; v2 = q2 - p; n2 = np.linalg.norm(v2)
            if n2 < .25 * L: continue
            nn = np.array([-v2[1], v2[0]]) / n2
            inl = np.abs((sel - p) @ nn) < 1.6
            if inl.sum() > bi: bi, best = inl.sum(), inl
        sel = sel[best]
        c = sel.mean(0); _, _, vt = np.linalg.svd(sel - c); dirv = vt[0]
        lines.append((c, dirv))
    def inter(l1, l2):
        (p, r), (q, s) = l1, l2
        M = np.array([r, -s]).T; t = np.linalg.solve(M, q - p); return p + t[0] * r
    return [inter(lines[3], lines[0]), inter(lines[0], lines[1]), inter(lines[1], lines[2]), inter(lines[2], lines[3])]

def coeffs(dst, src):
    A = []; B = []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; B += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(B, float)).tolist()

def status_bar(w, h, island):
    sb = Image.open(os.path.join(os.path.dirname(__file__), '..', 'barre-ios', 'sb-%d.png' % (1 if island else 0))).convert('RGBA')
    sb = sb.resize((w, h), Image.LANCZOS)
    bar = Image.new('RGBA', (w, h), (255, 255, 255, 255)); bar.alpha_composite(sb)
    return bar.convert('RGB')

def status_bar_old(w, h, island):
    bar = Image.new('RGB', (w, h), 'white'); d = ImageDraw.Draw(bar)
    f = ImageFont.truetype('/System/Library/Fonts/SFNS.ttf', int(h * .36))
    try: f.set_variation_by_axes([600])
    except Exception: pass
    d.text((w * .14, h * .56), '9:41', font=f, fill=(0, 0, 0), anchor='mm')
    x = w * .73; cy = h * .56; u = h * .07
    for i in range(4):  # réseau
        bh = u * (1.4 + i * .9); d.rounded_rectangle((x + i * u * 1.5, cy + u * 2 - bh, x + i * u * 1.5 + u, cy + u * 2), radius=u * .3, fill=(0, 0, 0))
    x += u * 7.5  # wifi
    for k, r in enumerate((u * 3.2, u * 2.1, u * 1.0)):
        d.arc((x - r, cy + u * 1.6 - r, x + r, cy + u * 1.6 + r), 225, 315, fill=(0, 0, 0), width=max(2, int(u * .75)))
    d.ellipse((x - u * .45, cy + u * 1.2, x + u * .45, cy + u * 2.1), fill=(0, 0, 0))
    x += u * 4.6  # batterie
    d.rounded_rectangle((x, cy - u * 1.3, x + u * 6.2, cy + u * 1.7), radius=u * .9, outline=(150, 150, 150), width=max(2, int(u * .35)))
    d.rounded_rectangle((x + u * .6, cy - u * .7, x + u * 5.6, cy + u * 1.1), radius=u * .5, fill=(0, 0, 0))
    d.rounded_rectangle((x + u * 6.5, cy - u * .3, x + u * 7.1, cy + u * .7), radius=u * .3, fill=(150, 150, 150))
    if island:
        iw, ih = w * .3, h * .5
        d.rounded_rectangle((w / 2 - iw / 2, h * .3, w / 2 + iw / 2, h * .3 + ih), radius=ih / 2, fill=(0, 0, 0))
    return bar

def run(photo, shot, out, island, nav=0):
    im = Image.open(photo).convert('RGB')
    # on travaille à la résolution d'affichage Retina : la photo est agrandie avant l'incrustation,
    # l'écran est donc posé net au lieu d'être agrandi avec elle
    up = float(os.environ.get('UP', '1'))
    if up != 1: im = im.resize((round(im.width * up), round(im.height * up)), Image.LANCZOS)
    W, H = im.size
    C = np.asarray(im).astype(np.float32)
    a = green_alpha(C)
    m = largest(a > .5)
    k = int(15 * up) | 1
    filled = Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(k)).filter(ImageFilter.MinFilter(k))
    q = fit_quad(np.asarray(filled) > 128)
    wq = (np.linalg.norm(q[1] - q[0]) + np.linalg.norm(q[2] - q[3])) / 2
    hq = (np.linalg.norm(q[3] - q[0]) + np.linalg.norm(q[2] - q[1])) / 2
    sw = 800; sh = int(sw * hq / wq)
    # téléphone vu très en biais (posé à plat) : le format apparent est faussé par la perspective,
    # RATIO=852/393 impose le vrai format de l'écran
    if os.environ.get('RATIO'): sh = int(sw * eval(os.environ['RATIO']))
    bh = round(sw * 54 / 393)  # barre d'état iOS : 54 pt sur 393
    ui = Image.open(shot).convert('RGB'); ow = ui.width; ui = ui.resize((sw, int(ui.height * sw / ui.width)), Image.LANCZOS)
    # écran iOS complet : barre d'état, contenu, barre d'onglets de l'app, puis la zone d'accueil (34 pt)
    hb = int(sw * .085)
    ch = sh - bh - hb
    scr = Image.new('RGB', (sw, sh), ui.getpixel((sw // 2, ui.height - 4)))
    navs = round(nav * sw / ow)
    if navs:
        scr.paste(ui.crop((0, 0, sw, ch - navs)), (0, bh))
        scr.paste(ui.crop((0, ui.height - navs, sw, ui.height)), (0, bh + ch - navs))
    else:
        scr.paste(ui.crop((0, 0, sw, ch)), (0, bh))
    d = ImageDraw.Draw(scr); hw, hh = sw * .34, sw * .013
    d.rounded_rectangle((sw / 2 - hw / 2, sh - hb * .42 - hh / 2, sw / 2 + hw / 2, sh - hb * .42 + hh / 2), radius=hh / 2, fill=(17, 17, 17))
    scr.paste(status_bar(sw, bh, island), (0, 0))
    # on réduit d'abord l'écran à sa taille finale (x1,5) pour un texte lissé, sans crénelage
    tw = max(int(wq * 2), 2); th = int(tw * sh / sw)
    scr = scr.resize((tw, th), Image.LANCZOS); sw, sh = tw, th
    src = [(0, 0), (sw, 0), (sw, sh), (0, sh)]
    warped = scr.transform((W, H), Image.PERSPECTIVE, coeffs([tuple(p) for p in q], src), Image.BICUBIC, fillcolor=(255, 255, 255))
    # où écrire : le vert (adouci), limité au contour bouché, et jamais sur les doigts
    region = np.asarray(filled.filter(ImageFilter.MaxFilter(3))) > 128
    A = (a * region)
    A = np.asarray(Image.fromarray((A * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.7))).astype(np.float32) / 255
    # verre : un reflet doux en diagonale
    yy, xx = np.mgrid[0:H, 0:W]; cx, cy = np.mean([p[0] for p in q]), np.mean([p[1] for p in q])
    gl = np.clip(((cx - xx) * .7 + (cy - yy)) / (hq * .9) + .15, 0, 1) * .10
    Wc = np.asarray(warped).astype(np.float32); Wc = Wc + (255 - Wc) * gl[..., None]
    # doigts et bords devant l'écran : on retire la part de vert mélangée à leur couleur
    rr, gg, bb = C[..., 0], C[..., 1], C[..., 2]
    # part de vert d'un pixel mêlé : la peau vaut environ -40, le vert du fond environ +247
    soft = np.clip((gg - np.maximum(rr, bb) + 38) / 285, 0, .985)
    soft = np.where(gg - np.maximum(rr, bb) < 6, 0, soft)
    key = np.median(C[(a > .97) & region], axis=0)
    F = (C - soft[..., None] * key) / (1 - soft[..., None])
    near = np.asarray(Image.fromarray((region * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(int(17 * up) | 1))) > 128
    F[..., 1] = np.where(near, np.minimum(F[..., 1], (F[..., 0] + F[..., 2]) / 2 + 2), F[..., 1])
    F = np.where(near[..., None], F, C).clip(0, 255)
    # devant l'écran (doigts), le bord se fond avec l'écran selon sa part de vert ; le long du cadre, masque serré
    inner = np.asarray(filled.filter(ImageFilter.MinFilter(int(9 * up) | 1))) > 128
    Ab = np.where(inner, np.maximum(A, soft), A)
    outc = F * (1 - Ab[..., None]) + Wc * Ab[..., None]
    Image.fromarray(outc.clip(0, 255).astype(np.uint8)).save(out)
    print(out, 'quad', [tuple(int(v) for v in p) for p in q], 'écran', sw, sh)

if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] == '1', int(sys.argv[5]) if len(sys.argv) > 5 else 0)
