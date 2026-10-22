import sys
from PIL import Image, ImageDraw
d, out = sys.argv[1], sys.argv[2]
fs=['A-38284854.jpg','B-25752284.jpg','C-21414936.jpg','D-7229076.jpg']
H=700; ims=[Image.open(f'{d}/{f}').convert('RGB') for f in fs]
ims=[i.resize((int(i.width*H/i.height),H)) for i in ims]
c=Image.new('RGB',(sum(i.width for i in ims)+30,H),'white'); x=0
for im in ims:
  dr=ImageDraw.Draw(im)
  for k in range(1,10): dr.line([(0,H*k/10),(im.width,H*k/10)],fill=(255,0,0)); dr.line([(im.width*k/10,0),(im.width*k/10,H)],fill=(255,0,0))
  c.paste(im,(x,0)); x+=im.width+10
c.save(out)
