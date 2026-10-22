import sys
from PIL import Image
S = sys.argv[1]
ims = []
for k in ['B-25752284', 'C-21414936', 'D-7229076']:
    im = Image.open(f'{S}/cut/{k}-cut.png').convert('RGBA')
    bg = Image.new('RGBA', im.size, (237, 244, 255, 255)); bg.alpha_composite(im)
    ims.append(bg.convert('RGB').resize((int(im.width * 700 / im.height), 700)))
c = Image.new('RGB', (sum(i.width for i in ims) + 20, 700), 'white'); x = 0
for i in ims: c.paste(i, (x, 0)); x += i.width + 10
c.save(f'{S}/cut/cutsheet.jpg')
