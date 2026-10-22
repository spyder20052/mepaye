# Exécuté dans build_pages.py après more_pages.py et aff_page.py : Développeurs sur le standard annexe.
def _feat2(ic, t):
    return f'<li><svg aria-hidden="true"><use href="#i-{ic}"/></svg><span>{t}</span></li>'

DV_ARCH = '''          <div class="fxh dvh" data-fxh aria-hidden="true">
            <div class="fxh__card is-on" data-fxh-s="0"><p class="fxh__k">Votre serveur</p><p class="dvh__ep"><span class="ep__m ep__m--post">POST</span><code>/api/v1/payments</code></p><pre class="dvh__pre">''' + hl('{\n  "amount": 5000,\n  "currency": "XOF",\n  "externalReference": "CMD-0142"\n}', 'json') + '''</pre></div>
            <div class="fxh__card" data-fxh-s="1"><p class="fxh__k">mepaye répond</p><p class="dvh__ep"><span class="ep__m ep__m--get">200</span><code>pending</code></p><pre class="dvh__pre">''' + hl('{\n  "status": "pending",\n  "payment_url":\n    "https://pay.mepaye.com/…"\n}', 'json') + '''</pre></div>
            <div class="fxh__card" data-fxh-s="2"><p class="fxh__k">Webhook signé</p><p class="dvh__ep"><span class="ep__m ep__m--post">POST</span><code>/webhooks/mepaye</code></p><pre class="dvh__pre">''' + hl('{\n  "event": "payment.succeeded",\n  "status": "PAID",\n  "amount": 5000\n}', 'json') + '''</pre><span class="m-tag m-tag--ok"><svg><use href="#i-check"/></svg>Signature vérifiée</span></div>
          </div>
          <ol class="fxh__steps" aria-hidden="true"><li class="is-on">Requête</li><li>Réponse</li><li>Webhook</li></ol>'''

DV_FLOW = [('layout', 'Votre site', 'Il crée le paiement.', False), ('', 'pay.mepaye.com', 'L’acheteur paie en Mobile Money ou par carte.', True),
           ('bell', 'Votre serveur', 'Webhook signé : vous livrez.', False), ('wallet', 'Votre wallet', 'Les fonds arrivent, moins 5 %.', False)]

dev_body = LOCAL_ICONS + '\n' + ax_hero('code', 'Développeurs · API Paiement',
    'Encaissez depuis<br> <em>votre propre site</em>.',
    'Un appel API, une page de paiement hébergée. Mobile Money et carte.',
    f'<a class="btn btn--lg" href="connexion.html">Créer ma clé API {ARROW}</a><a class="link" href="docs-paiement.html">Lire la documentation {CHEV}</a>',
    DV_ARCH, 'Exemple : votre serveur crée un paiement, mepaye répond avec la page de paiement, puis envoie un webhook signé.') + '\n' + ax_bar([
    ('parcours', 'Le parcours'), ('integration', 'Intégration'), ('api', 'Deux API'), ('webhooks', 'Webhooks'), ('questions', 'Questions')]) + f'''
    <section class="ax-sec" id="parcours" aria-labelledby="parcours-t" data-ax-chap>
      <div class="wrap">
{ax_head('Le parcours · 4 étapes', 'De votre site à votre wallet.', 'L’acheteur ne voit que pay.mepaye.com.', 'parcours-t')}
        <ol class="dv-flow af-flow" data-reveal>
          <span class="dv-flow__run" aria-hidden="true"><span class="dv-flow__tok">5 000 XOF</span></span>
''' + '\n'.join(f'''          <li class="dv-node" style="--d:{i * 2}s">
            <span class="dv-node__ic{' dv-node__ic--arch' if arch else ''}" aria-hidden="true">{'<img src="assets/brand/symbole.svg" alt="">' if arch else f'<svg><use href="#i-{ic}"/></svg>'}</span>
            <div><h3><span class="af-n">{i + 1}</span>{t}</h3><p>{p}</p></div>
          </li>''' for i, (ic, t, p, arch) in enumerate(DV_FLOW)) + f'''
        </ol>
      </div>
    </section>

    <section class="ax-sec ax-sec--soft" id="integration" aria-labelledby="integration-t" data-ax-chap>
      <div class="wrap">
{ax_head('Intégration · quelques lignes', 'Trois étapes, côté serveur.', 'Choisissez une étape, le code s’éclaire.', 'integration-t')}
        <div class="dv-ex dvx" data-reveal>
          <div>
            <ol class="dv-steps">
{_step(0, 'Créez une clé', 'Menu Développeur.')}
{_step(1, 'Créez le paiement', 'Depuis votre serveur.')}
{_step(2, 'Redirigez l’acheteur', 'Vers payment_url.')}
            </ol>
            <p class="dv-keep"><svg aria-hidden="true"><use href="#i-lock"/></svg>Gardez votre clé côté serveur, jamais dans le navigateur.</p>
          </div>
          <div>
            <div class="devwin devwin--solo" data-dv-code>
              <div class="devwin__code">
                <div class="dw__bar">
                  <span class="dw__file"><svg aria-hidden="true"><use href="#i-doc"/></svg><span data-ide-file>checkout.js</span></span>
                  <div class="dw__tabs" role="tablist" aria-label="Langage">
                    <button role="tab" type="button" aria-selected="true" data-lang="js" data-file="checkout.js">Node.js</button>
                    <button role="tab" type="button" aria-selected="false" data-lang="php" data-file="functions.php" tabindex="-1">WordPress</button>
                    <button role="tab" type="button" aria-selected="false" data-lang="curl" data-file="terminal" tabindex="-1">cURL</button>
                  </div>
                  <button type="button" class="dw__icon" data-ide-copy aria-label="Copier le code"><svg class="ic-copy" aria-hidden="true"><use href="#i-copy"/></svg><svg class="ic-ok" aria-hidden="true"><use href="#i-check"/></svg></button>
                </div>
{snippets(5000)}
              </div>
            </div>
            <p class="dv-note">Exemple simplifié. Tous les détails dans la <a href="docs-paiement.html#creer">documentation</a>.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="ax-sec ax-sec--pale" id="api" aria-labelledby="api-t" data-ax-chap>
      <div class="wrap">
{ax_head('Deux API · deux clés', 'Encaisser, ou lire vos données.', 'Une clé pour chacune.', 'api-t')}
        <div class="pkg pkg--2" data-reveal>
          <article class="pkg__c pkg__c--pro">
            <p class="pkg__tag">API Paiement<em>KYC requis</em></p>
            <p class="pkg__p">Encaisser<small>payments:write</small></p>
            <p class="pkg__d">Paiement hébergé, webhook signé.</p>
            <a class="pkg__cta" href="docs-paiement.html"><span>Lire la documentation</span><svg class="pkg__go" aria-hidden="true"><use href="#i-arrow"/></svg></a>
            <div class="pkg__use dvx__test"><p>Mode test, sans argent réel</p><div class="dvx__sim"><span class="dv-sim dv-sim--ok">Simuler un paiement réussi</span><span class="dv-sim">Simuler un échec</span></div><a class="dvx__try" href="paiement-test.html">Voir la page Mode test</a></div>
            <ul class="pkg__f">{_feat2('key', 'Clé mp_live_ ou mp_test_')}{_feat2('shield', 'Idempotence incluse')}{_feat2('clock', '100 requêtes par minute')}</ul>
          </article>
          <article class="pkg__c">
            <p class="pkg__tag">API Produits</p>
            <p class="pkg__p">Lire<small>*:read</small></p>
            <p class="pkg__d">Vos données, en lecture seule.</p>
            <a class="pkg__cta" href="docs-produits.html"><span>Lire la documentation</span><svg class="pkg__go" aria-hidden="true"><use href="#i-arrow"/></svg></a>
            <p class="dvx__res"><span>store</span><span>products</span><span>sales</span><span>customers</span><span>discounts</span><span>licenses</span></p>
            <ul class="pkg__f">{_feat2('key', 'Sans vérification d’identité')}{_feat2('layout', 'Pagination par curseur')}{_feat2('coins', 'Montants sans arrondi')}</ul>
          </article>
        </div>
      </div>
    </section>

    <section class="ax-sec" id="webhooks" aria-labelledby="webhooks-t" data-ax-chap>
      <div class="wrap">
{ax_head('Webhooks signés', 'Votre serveur est prévenu à chaque paiement.', 'Signés en HMAC-SHA256.', 'webhooks-t', ' <a href="docs-paiement.html#signature">Vérifier la signature</a>.')}
        <div class="dvw" data-reveal>
          <ul class="dvw__l">
            <li><span class="dvw__ic"><svg aria-hidden="true"><use href="#i-check"/></svg></span><span><b>payment.succeeded</b>Vous livrez.</span></li>
            <li><span class="dvw__ic dvw__ic--ko"><svg aria-hidden="true"><use href="#i-x"/></svg></span><span><b>payment.failed</b>Rien à livrer.</span></li>
            <li><span class="dvw__ic dvw__ic--n"><svg aria-hidden="true"><use href="#i-clock"/></svg></span><span><b>5 nouvelles tentatives</b>Sans réponse 2xx.</span></li>
          </ul>
          <div class="ax-plate dvw__plate"><div class="ax-plate__core dvw__core">
            <p class="dvw__h"><span><i class="dvw__dot"></i>Événements reçus</span><code>X-Mepaye-Signature: sha256=…</code></p>
            <ol class="log dv-log" data-dv-log aria-hidden="true">
              <li><time>10:42:08</time><span>payment.succeeded · 5 000 XOF</span><em>200</em></li>
              <li><time>10:42:31</time><span>payment.succeeded · 14 900 XOF</span><em>200</em></li>
              <li><time>10:43:02</time><span>payment.failed · 2 000 XOF</span><em>200</em></li>
            </ol>
          </div></div>
        </div>
      </div>
    </section>
''' + ax_faq([
    ('Faut-il un site codé sur mesure ?', 'Non. Tout site qui peut appeler une API depuis son serveur convient, WordPress compris.'),
    ('La vérification d’identité est-elle obligatoire ?', 'Oui pour l’API Paiement, qui encaisse de l’argent. Non pour l’API Produits, en lecture seule.'),
    ('Puis-je tester sans argent réel ?', 'Oui. Avec une clé mp_test_, la page de paiement propose de simuler un paiement réussi ou un échec.'),
    ('Combien ça coûte ?', 'Aucun abonnement. mepaye prélève 5 % sur chaque paiement encaissé. <a href="tarifs.html">Voir les tarifs</a>.'),
]) + '\n' + ax_end('Votre première vente par l’API.', 'Créez votre clé et commencez en mode test.', 'Créer ma clé API', 'connexion.html')

MORE_PAGES[0] = (MORE_PAGES[0][0], MORE_PAGES[0][1], MORE_PAGES[0][2], dev_body, MORE_PAGES[0][4])
