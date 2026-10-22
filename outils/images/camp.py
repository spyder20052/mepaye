import sys
from PIL import Image, ImageFilter
S, SITE = sys.argv[1], sys.argv[2]
C = S + '/camp'
# créatrice : même proportion et même cadrage que l'image d'origine, bords resserrés d'un pixel
im = Image.open(C + '/creatrice-cut.png').convert('RGBA')
a = im.getchannel('A').filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(.6)); im.putalpha(a)
w = 1060; h = round(w * 1192 / 941); x0 = 20; y0 = 20
im.crop((x0, y0, x0 + w, y0 + h)).save(SITE + '/assets/img/creatrice.webp', 'WEBP', quality=90, method=6)
# cartes : 4:5, à la taille d'affichage la plus grande (arche d'À propos)
for n in ['usage-abidjan', 'usage-cotonou', 'usage-dakar']:
    Image.open(f'{C}/{n}.webp').convert('RGB').resize((960, 1200), Image.LANCZOS).save(f'{SITE}/assets/img/{n}.webp', 'WEBP', quality=88, method=6)
# communauté : bande large
Image.open(C + '/communaute.webp').convert('RGB').save(SITE + '/assets/img/communaute.webp', 'WEBP', quality=88, method=6)
print('ok')
