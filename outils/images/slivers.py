import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
src, orig, out = sys.argv[1:4]
im = Image.open(src).convert('RGBA'); K = np.asarray(im).astype(np.float32)
O = np.asarray(Image.open(orig).convert('RGB')).astype(np.float32)
r, g, b = O[..., 0], O[..., 1], O[..., 2]; lum = .3 * r + .59 * g + .11 * b
bgness = np.clip((b - r - 16) / 10, 0, 1) * np.clip((lum - 160) / 20, 0, 1)
W, H = im.size
keep = Image.new('L', (W, H), 0); d = ImageDraw.Draw(keep)
d.ellipse((650 - 108, 262 - 118, 650 + 108, 262 + 118), fill=255)   # visage : yeux, dents
d.rectangle((90, 230, 340, 580), fill=255)                            # le téléphone et la main
keep = np.asarray(keep.filter(ImageFilter.GaussianBlur(6))).astype(np.float32) / 255
cut = bgness * (1 - keep)
cut = np.asarray(Image.fromarray((cut * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(.7))).astype(np.float32) / 255
K[..., 3] = K[..., 3] * (1 - cut)
Image.fromarray(K.clip(0, 255).astype(np.uint8)).save(out)
print('retirés', int((cut > .5).sum()))
