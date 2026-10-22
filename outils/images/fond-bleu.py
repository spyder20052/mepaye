"""Fait passer le mur beige de la photo au bleu pâle des panneaux du site (#EAF4FE).
Sur les bords (pull, mains, cadre), seule la part de mur contenue dans chaque pixel change de couleur."""
import sys, numpy as np, cv2
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
im = np.asarray(Image.open(src).convert('RGB')).astype(np.float32) / 255
lab = cv2.cvtColor(im, cv2.COLOR_RGB2Lab); L, a, b = lab[..., 0], lab[..., 1], lab[..., 2]
C = np.hypot(a, b)
ss = lambda x, e0, e1: np.clip((x - e0) / (e1 - e0), 0, 1)
core = (ss(L, 72, 80) * ss(C, 24, 16)) > .5
# l'écran : le vert de la photo d'origine (même cadrage, agrandi à la taille de la sortie)
G = np.asarray(Image.open(sys.argv[3]).convert('RGB').resize((im.shape[1], im.shape[0]), Image.BILINEAR)).astype(int)
green = (G[..., 1] - np.maximum(G[..., 0], G[..., 2])) > 40
screen = cv2.dilate(green.astype(np.uint8), np.ones((7, 7), np.uint8)) > 0
core &= ~screen
# couleur du mur, lissée : elle varie doucement (dégradé)
Lb = cv2.GaussianBlur(np.where(core, L, 0), (0, 0), 40) / np.maximum(cv2.GaussianBlur(core.astype(np.float32), (0, 0), 40), 1e-3)
ab_ = [cv2.GaussianBlur(np.where(core, c, 0), (0, 0), 40) / np.maximum(cv2.GaussianBlur(core.astype(np.float32), (0, 0), 40), 1e-3) for c in (a, b)]
# part de mur dans chaque pixel : entre le plus sombre du voisinage (le sujet) et la luminosité du mur
Lmin = cv2.erode(L, np.ones((15, 15), np.uint8))
f = np.clip((L - Lmin) / np.maximum(Lb - Lmin, 4), 0, 1)
near = cv2.dilate(core.astype(np.uint8), np.ones((25, 25), np.uint8)) > 0
f = np.where(core, 1, np.where(near & ~screen, f, 0))
f = cv2.GaussianBlur(f.astype(np.float32), (0, 0), .8)
t = cv2.cvtColor(np.float32([[[234, 244, 254]]]) / 255, cv2.COLOR_RGB2Lab)[0, 0]
L2 = L + f * (t[0] - Lb) * .85
a2 = a + f * (t[1] - ab_[0]); b2 = b + f * (t[2] - ab_[1])
out = cv2.cvtColor(np.stack([L2, a2, b2], -1).astype(np.float32), cv2.COLOR_Lab2RGB)
Image.fromarray((out.clip(0, 1) * 255 + .5).astype(np.uint8)).save(dst)
