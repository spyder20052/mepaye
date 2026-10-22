import sys, os
from PIL import Image
d, out = sys.argv[1], sys.argv[2]
fs = ['creatrice','usage-abidjan','usage-cotonou','usage-dakar','mains','communaute']
H = 640; ims = []
for f in fs:
    im = Image.open(f'{d}/{f}.webp').convert('RGB'); ims.append(im.resize((int(im.width*H/im.height), H)))
c = Image.new('RGB', (sum(i.width for i in ims) + 50, H), 'white'); x = 0
for i in ims: c.paste(i, (x, 0)); x += i.width + 10
c.save(out)
