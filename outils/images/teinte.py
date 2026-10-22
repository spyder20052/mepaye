"""Change la couleur d'une miniature : les bleus (fond, socle, coque, pastille, titre) prennent la teinte du type,
la peau, les blancs et les gris restent intacts. Rotation de teinte dans l'espace Lab (luminosité conservée)."""
import sys, numpy as np, cv2
from PIL import Image
def lab_hue(hexc):
    c = np.uint8([[[int(hexc[i:i+2], 16) for i in (1, 3, 5)]]]).astype(np.float32) / 255
    L, a, b = cv2.cvtColor(c, cv2.COLOR_RGB2Lab)[0, 0]
    return np.degrees(np.arctan2(b, a))
def run(src, dst, target, sat=1.0):
    im = np.asarray(Image.open(src).convert('RGB')).astype(np.float32) / 255
    lab = cv2.cvtColor(im, cv2.COLOR_RGB2Lab)
    L, a, b = lab[..., 0], lab[..., 1], lab[..., 2]
    C = np.hypot(a, b); h = np.degrees(np.arctan2(b, a))
    src_h = lab_hue('#0866FF'); d = lab_hue(target) - src_h
    # poids : 1 pour les bleus (±35° autour du cobalt), fondu jusqu'à ±60°, rien pour les couleurs neutres
    dist = np.abs(((h - src_h) + 180) % 360 - 180)
    w = np.clip((100 - dist) / 20, 0, 1) * np.clip((C - 1) / 3, 0, 1)
    nh = np.radians(h + d * w)
    C2 = C * (1 + (sat - 1) * w)
    lab2 = np.stack([L, C2 * np.cos(nh), C2 * np.sin(nh)], -1)
    out = cv2.cvtColor(lab2.astype(np.float32), cv2.COLOR_Lab2RGB)
    Image.fromarray((out.clip(0, 1) * 255 + .5).astype(np.uint8)).save(dst)
if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]) if len(sys.argv) > 4 else 1.0)
