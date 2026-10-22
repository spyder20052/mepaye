# Exécuté dans build_pages.py après more_pages.py : Créer un ebook sur le standard annexe, épuré.
_EBH = [('moderne', 'Moderne'), ('afrique', 'Afrique'), ('luxe', 'Luxe')]
EB_ARCH = '          <div class="fxh ebh" data-fxh aria-hidden="true">\n' + '\n'.join(
    f'''            <div class="fxh__card{' is-on' if i == 0 else ''}" data-fxh-s="{i}"><div class="eb__cover eb__cover--{k}"><i class="eb__arch"></i><i class="eb__motif"></i><span class="eb__tag">Ebook</span><b>Cuisiner léger</b><small>Aïcha K.</small></div><p class="bl-c__m"><span class="pkg__tag">{n}</span><span>PDF · DOCX</span></p></div>'''
    for i, (k, n) in enumerate(_EBH)) + '''
          </div>
          <ol class="fxh__steps" aria-hidden="true"><li class="is-on">Moderne</li><li>Afrique</li><li>Luxe</li></ol>'''

_eb_demo = ebook_body[ebook_body.index('        <div class="eb" data-eb data-reveal>'):ebook_body.index('      </div>\n    </section>', ebook_body.index('        <div class="eb" data-eb data-reveal>'))]

def _eb_tile(vis, t, p):
    return f'''          <article class="tsa__c" data-reveal>
            <div class="ax-plate"><div class="ax-plate__core tsa__v">{vis}</div></div>
            <h3>{t}</h3>
            <p>{p}</p>
          </article>'''

_v_live = '<div class="m-card ebt-live"><p class="fxh__k">Chapitre 2</p><b class="ebt-live__t">Le placard idéal</b><span class="m-lines m-type ebt-type"><i style="--w:96%"></i><i style="--w:88%"></i><i style="--w:70%"></i></span><span class="m-tag m-tag--ok"><span class="m-dot"></span>Écriture en direct</span></div>'
_v_designs = '<div class="ebt-covers">' + ''.join(f'<span class="eb__cover eb__cover--{k}"><i class="eb__arch"></i><i class="eb__motif"></i></span>' for k in ('moderne', 'afrique', 'wellness', 'luxe')) + '</div><span class="m-tag">Plus de 15 designs</span>'
_v_files = '<div class="ebt-files"><span class="ebt-file"><b>PDF</b><small>Prêt à vendre</small></span><span class="ebt-file ebt-file--docx"><b>DOCX</b><small>Modifiable</small></span></div>'

ebook_body2 = LOCAL_ICONS + '\n' + ax_hero('spark', 'IA · Propulsé par Claude',
    'Votre ebook pro,<br> <em>en 10 minutes</em>.',
    'Un sujet, un style. L’IA écrit, vous relisez.',
    f'<a class="btn btn--lg" href="inscription.html">Créer mon ebook {ARROW}</a><a class="link" href="#demo">Voir la démo {CHEV}</a>',
    EB_ARCH, 'Exemples de couvertures dans trois styles.') + '\n' + ax_bar([
    ('demo', 'Démo'), ('inclus', 'Inclus'), ('prix', 'Prix'), ('questions', 'Questions')]) + f'''
    <section class="ax-sec" id="demo" aria-labelledby="demo-t" data-ax-chap>
      <div class="wrap">
{ax_head('Démo · en direct', 'Choisissez un style.', 'La couverture change, les chapitres s’écrivent.', 'demo-t')}
{_eb_demo}      </div>
    </section>

    <section class="ax-sec ax-sec--soft" id="inclus" aria-labelledby="inclus-t" data-ax-chap>
      <div class="wrap">
{ax_head('Inclus · dans chaque ebook', 'Prêt à vendre.', 'Rédaction, design et fichiers.', 'inclus-t')}
        <div class="tsa">
{_eb_tile(_v_live, 'Écriture en direct', 'Chaque chapitre s’écrit sous vos yeux.')}
{_eb_tile(_v_designs, 'Des designs pro', 'Moderne, afrique, wellness, luxe…')}
{_eb_tile(_v_files, 'PDF et DOCX', 'Sommaire, pagination, modifiable dans Word.')}
        </div>
      </div>
    </section>

    <section class="ax-sec ax-sec--pale" id="prix" aria-labelledby="prix-t" data-ax-chap>
      <div class="wrap">
{ax_head('Prix · en crédits IA', 'Vous payez à la création.', 'Sans abonnement.', 'prix-t', ' <a href="tarifs.html#credits">Voir les packs</a>.')}
        <div class="pkg ebp" data-reveal>
          <article class="pkg__c">
            <p class="pkg__tag">Description</p>
            <p class="pkg__p">5<small>crédits</small></p>
            <p class="pkg__d">Un texte de vente pour votre produit.</p>
          </article>
          <article class="pkg__c pkg__c--pro">
            <p class="pkg__tag">Ebook<em>Complet</em></p>
            <p class="pkg__p">50<small>crédits</small></p>
            <p class="pkg__d">Plan, rédaction, couverture, PDF et DOCX.</p>
            <div class="pkg__use"><p>Le Pack Découverte</p><div><span><svg aria-hidden="true"><use href="#i-spark"/></svg><b>100</b> crédits</span><span><svg aria-hidden="true"><use href="#i-coins"/></svg><b>2 500</b> XOF</span></div></div>
            <a class="pkg__cta" href="inscription.html"><span>Créer mon ebook</span><svg class="pkg__go" aria-hidden="true"><use href="#i-arrow"/></svg></a>
          </article>
          <article class="pkg__c">
            <p class="pkg__tag">Formation</p>
            <p class="pkg__p">80<small>crédits</small></p>
            <p class="pkg__d">Modules et leçons, prêts à publier.</p>
          </article>
        </div>
      </div>
    </section>
''' + ax_faq([
    ('Puis-je modifier le texte ?', 'Oui, dans l’éditeur intégré, ou dans Word avec le fichier DOCX.'),
    ('Combien de temps faut-il ?', 'Quelques minutes, selon la longueur de l’ebook.'),
    ('L’IA remplace-t-elle mon expertise ?', 'Non. Elle structure et rédige. Vos exemples et votre voix font la différence.'),
    ('Puis-je payer avec mes ventes ?', 'Oui. Payez vos crédits depuis votre wallet : 10 % de crédits en plus.'),
]) + '\n' + ax_end('Votre premier ebook, aujourd’hui.', 'Un sujet suffit pour commencer.', 'Créer mon ebook', 'inscription.html')

for _i, _pg in enumerate(MORE_PAGES):
    if _pg[0] == 'creer-ebook.html':
        MORE_PAGES[_i] = (_pg[0], _pg[1], _pg[2], ebook_body2, _pg[4])
