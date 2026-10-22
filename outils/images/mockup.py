"""Incruste un ou plusieurs écrans de l'app dans les écrans verts d'un mockup.
Usage : mockup.py photo sortie écran1.png[:nav] [écran2.png[:nav] ...]
Les écrans sont attribués de gauche à droite. Un écran coupé par le bas de l'image est prolongé
avec les proportions réelles d'un iPhone (393 × 852 pt). L'île dynamique de la photo est gardée."""
import sys, os
import numpy as np
from collections import deque
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, os.path.dirname(__file__))
from greenscreen import green_alpha, fit_quad, coeffs, status_bar

RATIO = 852 / 393

def components(mask, n):
    k = 4; h, w = mask.shape
    small = np.asarray(Image.fromarray((mask * 255).astype(np.uint8)).resize((w // k, h // k), Image.BOX)) > 128
    sh, sw = small.shape; lab = np.zeros((sh, sw), np.int32); sizes = []; cur = 0
    for y in range(sh):
        for x in range(sw):
            if small[y, x] and not lab[y, x]:
                cur += 1; q = deque([(y, x)]); lab[y, x] = cur; c = 0
                while q:
                    cy, cx = q.popleft(); c += 1
                    for ny, nx in ((cy+1,cx),(cy-1,cx),(cy,cx+1),(cy,cx-1)):
                        if 0 <= ny < sh and 0 <= nx < sw and small[ny, nx] and not lab[ny, nx]:
                            lab[ny, nx] = cur; q.append((ny, nx))
                sizes.append((c, cur))
    keep = [l for _, l in sorted(sizes, reverse=True)[:n]]
    big = np.asarray(Image.fromarray(lab.astype(np.int32)).resize((w, h), Image.NEAREST))
    out = []
    for l in keep:
        m = (big == l)
        m = np.asarray(Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(9))) > 0
        out.append(m & mask)
    out.sort(key=lambda m: np.nonzero(m)[1].mean())
    return out

def build_screen(shot, nav, tw):
    sw = 800; sh = round(sw * RATIO)
    bh = round(sw * 54 / 393); hb = round(sw * 34 / 393)
    ui = Image.open(shot).convert('RGB'); ow = ui.width; ui = ui.resize((sw, round(ui.height * sw / ui.width)), Image.LANCZOS)
    ch = sh - bh - hb
    scr = Image.new('RGB', (sw, sh), ui.getpixel((sw // 2, ui.height - 4)))
    navs = round(nav * sw / ow)
    if navs:
        scr.paste(ui.crop((0, 0, sw, ch - navs)), (0, bh)); scr.paste(ui.crop((0, ui.height - navs, sw, ui.height)), (0, bh + ch - navs))
    else:
        scr.paste(ui.crop((0, 0, sw, min(ch, ui.height))), (0, bh))
    d = ImageDraw.Draw(scr); hw, hh = sw * .34, sw * .013
    d.rounded_rectangle((sw / 2 - hw / 2, sh - hb * .42 - hh / 2, sw / 2 + hw / 2, sh - hb * .42 + hh / 2), radius=hh / 2, fill=(17, 17, 17))
    scr.paste(status_bar(sw, bh, False), (0, 0))
    th = round(tw * RATIO)
    return scr.resize((tw, th), Image.LANCZOS)

def ransac_line(P):
    rng = np.random.default_rng(7); best, bi = None, -1
    for _ in range(500):
        i, j = rng.choice(len(P), 2, replace=False)
        p, q2 = P[i], P[j]; v = q2 - p; n2 = np.linalg.norm(v)
        if n2 < 20: continue
        nn = np.array([-v[1], v[0]]) / n2
        inl = np.abs((P - p) @ nn) < 1.6
        if inl.sum() > bi: bi, best = inl.sum(), inl
    S_ = P[best]; c = S_.mean(0); _, _, vt = np.linalg.svd(S_ - c)
    return c, vt[0]

def inter(l1, l2):
    (p, r), (q, s) = l1, l2
    t = np.linalg.solve(np.array([r, -s]).T, q - p); return p + t[0] * r

def fit_occluded(fm, occ, H, W):
    # côtés repérés par la normale du contour ; un côté caché devient la parallèle au côté opposé
    G = np.asarray(Image.fromarray((fm * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2))).astype(np.float32) / 255
    gy, gx = np.gradient(G)
    ys, xs = np.nonzero((G > .35) & (G < .65))
    keep = (ys > 3) & (ys < H - 4) & (xs > 3) & (xs < W - 4)
    ys, xs = ys[keep], xs[keep]
    n = -np.stack([gx[ys, xs], gy[ys, xs]], 1); n /= np.linalg.norm(n, axis=1, keepdims=True) + 1e-9
    P = np.stack([xs, ys], 1).astype(float)
    sides = {'t': n[:, 1] < -.85, 'b': n[:, 1] > .85, 'l': n[:, 0] < -.85, 'r': n[:, 0] > .85}
    L = {k: ransac_line(P[v]) for k, v in sides.items() if k not in occ and v.sum() > 30}
    my, mx = np.nonzero(fm); M = np.stack([mx, my], 1).astype(float)
    opp = {'r': 'l', 'l': 'r', 'b': 't', 't': 'b'}
    for k in occ:
        c, d = L[opp[k]]
        nn = np.array([-d[1], d[0]])
        if k == 'b':
            if nn[1] < 0: nn = -nn
            tl, tr = inter(L['l'], L['t']), inter(L['r'], L['t'])
            off = np.linalg.norm(tr - tl) * RATIO
            L[k] = (c + nn * off, d)
        else:
            if (k == 'r') != (nn[0] > 0): nn = -nn
            off = ((M - c) @ nn).max()
            L[k] = (c + nn * off, d)
    return [inter(L['l'], L['t']), inter(L['t'], L['r']), inter(L['r'], L['b']), inter(L['b'], L['l'])]

def quad_for(m, H, occ=''):
    up = float(os.environ.get('UP', '1'))
    k = int(15 * up) | 1
    filled = Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(k)).filter(ImageFilter.MinFilter(k))
    fm = np.asarray(filled) > 128
    q = fit_occluded(fm, occ, H, fm.shape[1]) if occ else fit_quad(fm)
    return [np.array(p, float) for p in q], filled

def main():
    photo, out = sys.argv[1], sys.argv[2]
    shots = [((s.split(':') + ['0', ''])[0], int((s.split(':') + ['0', ''])[1] or 0), (s.split(':') + ['0', ''])[2]) for s in sys.argv[3:]]
    up = float(os.environ.get('UP', '1'))
    im = Image.open(photo).convert('RGB')
    if up != 1: im = im.resize((round(im.width * up), round(im.height * up)), Image.LANCZOS)
    W, H = im.size; C = np.asarray(im).astype(np.float32)
    a = green_alpha(C)
    comps = components(a > .5, len(shots))
    outc = C.copy()
    screens = np.zeros(C.shape[:2], bool)
    rr, gg, bb = C[..., 0], C[..., 1], C[..., 2]
    soft = np.clip((gg - np.maximum(rr, bb) + 38) / 285, 0, .985); soft = np.where(gg - np.maximum(rr, bb) < 6, 0, soft)
    for m, (shot, nav, occ) in zip(comps, shots):
        q, filled = quad_for(m, H, occ)
        wq = (np.linalg.norm(q[1] - q[0]) + np.linalg.norm(q[2] - q[3])) / 2
        hq = (np.linalg.norm(q[3] - q[0]) + np.linalg.norm(q[2] - q[1])) / 2
        tw = max(int(max(wq, hq / RATIO) * 2), 4)
        scr = build_screen(shot, nav, tw); sw, sh = scr.size
        warped = scr.transform((W, H), Image.PERSPECTIVE, coeffs([tuple(p) for p in q], [(0, 0), (sw, 0), (sw, sh), (0, sh)]), Image.BICUBIC, fillcolor=(255, 255, 255))
        region = np.asarray(filled.filter(ImageFilter.MaxFilter(3))) > 128
        A = a * region
        A = np.asarray(Image.fromarray((A * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.7))).astype(np.float32) / 255
        key = np.median(C[(a > .97) & region], axis=0)
        F = (C - soft[..., None] * key) / (1 - soft[..., None])
        near = np.asarray(Image.fromarray((region * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(int(17 * up) | 1))) > 128
        F[..., 1] = np.where(near, np.minimum(F[..., 1], (F[..., 0] + F[..., 2]) / 2 + 2), F[..., 1])
        F = np.where(near[..., None], F, outc).clip(0, 255)
        inner = np.asarray(filled.filter(ImageFilter.MinFilter(int(9 * up) | 1))) > 128
        Ab = np.where(inner, np.maximum(A, soft), A)
        Wc = np.asarray(warped).astype(np.float32)
        # léger reflet de verre en diagonale
        yy, xx = np.mgrid[0:H, 0:W]; cx, cy = np.mean([p[0] for p in q]), np.mean([p[1] for p in q])
        gl = np.clip(((cx - xx) * .7 + (cy - yy)) / (hq * .9) + .15, 0, 1) * .06
        Wc = Wc + (255 - Wc) * gl[..., None]
        outc = np.where(near[..., None], F * (1 - Ab[..., None]) + Wc * Ab[..., None], outc)
        screens |= inner
        print(os.path.basename(shot), 'quad', [tuple(int(v) for v in p) for p in q])
    # vert résiduel sur la scène (reflet du sol, liserés) : neutralisé
    r, g, b = outc[..., 0], outc[..., 1], outc[..., 2]
    over = g - np.maximum(r, b)
    outc[..., 1] = np.where((over > 4) & ~screens, np.maximum(r, b) + np.minimum(over, 4), g)
    Image.fromarray(outc.clip(0, 255).astype(np.uint8)).save(out)

if __name__ == '__main__':
    main()
