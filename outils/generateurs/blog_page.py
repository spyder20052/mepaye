# Exécuté dans build_pages.py après la section Blog d'origine : le blog sur le standard annexe, épuré.
import math as _m, re as _rb, json as _jb
_MIN = {}
for _k, _v in _jb.load(open(str(pathlib.Path(__file__).resolve().parent) + '/articles.json')).items():
    if _k.startswith('blog/'):
        _MIN[_v['slug']] = max(1, _m.ceil(len(_rb.sub('<[^>]+>', ' ', _v['body']).split()) / 200))
BL_SHORT = {'creer-ebook-vendre-afrique-francophone': 'Créer un ebook qui se vend',
            'mobile-money-creators-wave-orange-mtn': 'Mobile Money : le guide complet',
            'lancer-premier-produit-digital-7-jours': 'Votre premier produit en 7 jours',
            'vendre-formation-en-ligne-afrique': 'Vendre ses formations en ligne',
            'affiliation-multiplier-revenus-createur': 'Multiplier ses revenus par l’affiliation'}
BL_LINE = {'creer-ebook-vendre-afrique-francophone': 'De l’idée à la mise en vente.',
           'mobile-money-creators-wave-orange-mtn': 'Wave, Orange Money, MTN : frais et choix.',
           'lancer-premier-produit-digital-7-jours': 'Une feuille de route, jour par jour.',
           'vendre-formation-en-ligne-afrique': 'Structurer, fixer le prix, encaisser.',
           'affiliation-multiplier-revenus-createur': 'Vos clients vendent pour vous.'}

def _bl_card(i, cat, tag, t, p, slug, cv, art):
    return f'''          <article class="bl-c{' bl-c--wide' if i == 0 else ''}" data-cat="{cat}" data-reveal>
            <a href="article-{slug}.html">
              <span class="bl-c__cv"><span class="cover {cv}" aria-hidden="true">{art}</span></span>
              <span class="bl-c__b">
                <span class="bl-c__m"><span class="pkg__tag">{tag}</span><span>{_MIN.get(slug, 5)} min</span></span>
                <b>{BL_SHORT.get(slug, t)}</b>
                <span class="bl-c__p">{BL_LINE.get(slug, '')}</span>
                <span class="bl-c__go">Lire le guide <svg aria-hidden="true"><use href="#i-arrow"/></svg></span>
                <span class="sr-only">{t}</span>
              </span>
            </a>
          </article>'''

_hero_posts = [POSTS[0], POSTS[1], POSTS[2]]
BL_ARCH = '          <div class="fxh blh" data-fxh aria-hidden="true">\n' + '\n'.join(
    f'''            <div class="fxh__card{' is-on' if i == 0 else ''}" data-fxh-s="{i}"><span class="blh__cv"><span class="cover {cv}">{art}</span></span><p class="bl-c__m"><span class="pkg__tag">{tag}</span><span>{_MIN.get(slug, 5)} min</span></p><b class="blh__t">{BL_SHORT[slug]}</b></div>'''
    for i, (cat, tag, t, p, slug, cv, art) in enumerate(_hero_posts)) + '''
          </div>
          <ol class="fxh__steps" aria-hidden="true"><li class="is-on">Ebook</li><li>Paiements</li><li>7 jours</li></ol>'''

_filters = [('all', 'Tout'), ('guides', 'Guides'), ('paiements', 'Paiements'), ('formations', 'Formations'), ('affiliation', 'Affiliation')]
blog_body = ax_hero('book', 'Blog · 5 guides',
    'Apprenez à<br> <em>vendre votre savoir</em>.',
    'Des guides concrets, pour l’Afrique francophone.',
    f'<a class="btn btn--lg" href="article-{POSTS[0][4]}.html">Lire le dernier guide {ARROW}</a><a class="link" href="#guides">Tous les guides {CHEV}</a>',
    BL_ARCH, 'Exemples de guides du blog.') + '\n' + ax_bar([('guides', 'Les guides'), ('commencer', 'Commencer')]) + f'''
    <section class="ax-sec ax-sec--pale" id="guides" aria-labelledby="guides-t" data-ax-chap>
      <div class="wrap">
{ax_head('Les guides · 5 articles', 'Pour vendre, pas à pas.', 'Choisissez un thème.', 'guides-t')}
        <div class="bl-f" role="group" aria-label="Filtrer par thème" data-reveal>{''.join(f'<button type="button" aria-pressed="{str(k == "all").lower()}" data-filter="{k}">{n}</button>' for k, n in _filters)}</div>
        <div class="bl-g">
{chr(10).join(_bl_card(i, *p_) for i, p_ in enumerate(POSTS))}
        </div>
      </div>
    </section>

    <div id="commencer" data-ax-chap>
''' + ax_end('Prêt à vendre votre savoir ?', 'Votre boutique est gratuite, en ligne en quelques minutes.', 'Commencer gratuitement', 'inscription.html') + '''
    </div>
'''
