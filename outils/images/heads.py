import sys
from PIL import Image
for f in sys.argv[1:]:
    a = Image.open(f).convert('RGBA').getchannel('A'); w, h = a.size; bb = a.getbbox()
    top = bb[1]; row = a.crop((0, top, w, top + int((bb[3]-top)*.08))).getbbox()
    print(f.split('/')[-1], 'size', (w, h), 'bbox', bb, 'head x', (row[0]+row[2])/2/w if row else None, 'top', top/h)
