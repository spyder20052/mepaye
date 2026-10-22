"""Menu mobile commun : de grands liens typographiques, des filets pointillés,
la page en cours en bleu, le compte en bas, le symbole en filigrane."""
MENU = [('/fonctionnalites', 'fonctionnalites.html', 'Fonctionnalités'), ('/tarifs', 'tarifs.html', 'Tarifs'),
        ('/affiliation', 'affiliation.html', 'Affiliation'), ('/developpeurs', 'developpeurs.html', 'Développeurs'),
        ('/aide', 'aide.html', 'Aide'), ('/blog', 'blog.html', 'Blog')]

def menu_html(current=None):
    rows = ''.join(
        f'<li><a href="{h}"{" aria-current=" + chr(34) + "page" + chr(34) if current == f else ""}><span>{t}</span><svg aria-hidden="true"><use href="#i-arrow"/></svg></a></li>'
        for h, f, t in MENU)
    return f'''  <div class="menu" id="menu" data-menu hidden>
    <nav class="menu__in" aria-label="Menu mobile">
      <ul class="menu__big">{rows}</ul>
      <div class="menu__cta"><a class="menu__login" href="/connexion">Connexion</a><a class="btn btn--lg" href="/inscription">Commencer gratuitement <span class="btn__ic" aria-hidden="true"><svg><use href="#i-arrow"/></svg></span></a></div>
      <p class="menu__foot"><a href="/a-propos">À propos</a><a href="/contact">Contact</a><a href="/boutique">Boutique de démo</a></p>
    </nav>
    <img class="menu__mark" src="/assets/brand/symbole.svg" alt="" aria-hidden="true">
  </div>'''
