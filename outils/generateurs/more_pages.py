# Exécuté dans build_pages.py : hero, band, icon, ARROW, CHEV, CHECK, idx sont disponibles.
import sys as _sys
_sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import importlib as _il, codegen as _cg
_il.reload(_cg)
cb, snippets, hl = _cg.cb, _cg.snippets, _cg.hl

X = '<svg aria-hidden="true"><use href="#i-x"/></svg>'
LOCAL_ICONS = '''  <svg width="0" height="0" style="position:absolute" aria-hidden="true">
    <symbol id="i-x" viewBox="0 0 24 24"><path d="M7 7l10 10M17 7 7 17"/></symbol>
    <symbol id="i-key" viewBox="0 0 24 24"><circle cx="8" cy="15" r="3.5"/><path d="m10.5 12.5 8-8M16 7l2.5 2.5M14 9l2 2"/></symbol>
    <symbol id="i-flask" viewBox="0 0 24 24"><path d="M9.5 4h5M10.5 4v5.5L5.6 17.6A1.6 1.6 0 0 0 7 20h10a1.6 1.6 0 0 0 1.4-2.4l-4.9-8.1V4"/><path d="M7.8 14.5h8.4"/></symbol>
    <symbol id="i-code" viewBox="0 0 24 24"><path d="m8.5 8-4 4 4 4M15.5 8l4 4-4 4M13.5 5.5l-3 13"/></symbol>
    <symbol id="i-pen" viewBox="0 0 24 24"><path d="M4.5 19.5 5.5 15 15.5 5a2.1 2.1 0 0 1 3 3l-10 10z"/><path d="M13.5 7l3 3"/></symbol>
    <symbol id="i-trash" viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.5h5V7M6.5 7l1 12.5h9l1-12.5"/></symbol>
    <symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></symbol>
  </svg>'''

# ================================================================== Développeurs (vue d'ensemble)
def _node(ic, t, p, d, arch=False):
    inner = '<img src="assets/brand/symbole.svg" alt="">' if arch else f'<svg><use href="#i-{ic}"/></svg>'
    return f'''          <li class="dv-node" style="--d:{d}s">
            <span class="dv-node__ic{' dv-node__ic--arch' if arch else ''}" aria-hidden="true">{inner}</span>
            <div><h3>{t}</h3><p>{p}</p></div>
          </li>'''

def _step(i, t, p):
    return f'''            <li><button type="button" aria-pressed="false" data-dv-step="{i}"><span class="dv-n">{i + 1}</span><span><b>{t}</b><small>{p}</small></span></button></li>'''

def _q(q, a):
    return f'''          <details><summary>{q}</summary><p>{a}</p></details>'''

dev_body = LOCAL_ICONS + '\n' + hero('Développeurs · API Paiement', 'Encaissez depuis <em>votre propre site</em>.',
    'Un appel à l’API, une page de paiement hébergée. Vos clients paient en Mobile Money ou par carte.',
    f'''        <div class="pg-ctas">
          <a class="btn btn--lg" href="connexion.html">Créer ma clé API {ARROW}</a>
          <a class="link" href="docs-paiement.html">Lire la documentation {CHEV}</a>
        </div>
        <div class="dv-rr" role="img" aria-label="Exemple : votre serveur crée un paiement de 5 000 XOF, mepaye répond avec l’adresse de la page de paiement." data-reveal>
          <div class="dv-rr__p">
            <p class="dv-rr__h"><span class="dv-m">POST</span><span class="dv-path">/api/v1/payments</span></p>
<pre>{hl("""{
  "amount": 5000,
  "currency": "XOF",
  "externalReference": "CMD-0142"
}""", 'json')}</pre>
          </div>
          <span class="dv-rr__dot" aria-hidden="true"></span>
          <div class="dv-rr__p dv-rr__res">
            <p class="dv-rr__h"><span class="dv-m dv-m--ok">pending</span><span class="dv-path">Réponse</span></p>
<pre><span class="l" style="--i:0"><span class="p">{{</span></span>
<span class="l" style="--i:1">  <span class="k">"status"</span><span class="p">:</span> <span class="s">"pending"</span><span class="p">,</span></span>
<span class="l" style="--i:2">  <span class="k">"payment_url"</span><span class="p">:</span></span>
<span class="l" style="--i:3">    <span class="s">"https://pay.mepaye.com/checkout/…"</span></span>
<span class="l" style="--i:4"><span class="p">}}</span></span></pre>
          </div>
        </div>''') + f'''
    <section class="pg-sec" aria-labelledby="dv-flow-t">
      <div class="wrap">
        <header class="pg-head pg-head--center" data-reveal><p class="kicker">Le parcours</p><h2 class="h2" id="dv-flow-t">De votre site à votre wallet.</h2></header>
        <ol class="dv-flow" data-reveal>
          <span class="dv-flow__run" aria-hidden="true"><span class="dv-flow__tok">5 000 XOF</span></span>
{_node('layout', 'Votre site', 'Il crée le paiement.', 0)}
{_node('', 'pay.mepaye.com', 'L’acheteur paie en Mobile Money ou par carte.', 2, arch=True)}
{_node('bell', 'Votre serveur', 'Webhook signé : vous livrez.', 4)}
{_node('wallet', 'Votre wallet', 'Les fonds arrivent, moins 5 %.', 6)}
        </ol>
      </div>
    </section>

    <section class="pg-sec pg-sec--tight" id="exemples" aria-labelledby="dv-ex-t">
      <div class="wrap">
        <div class="dv-ex">
          <div data-reveal>
            <p class="kicker">Intégration</p>
            <h2 class="h2" id="dv-ex-t">Trois étapes, quelques lignes.</h2>
            <ol class="dv-steps">
{_step(0, 'Créez une clé', 'Menu Développeur, après vérification d’identité.')}
{_step(1, 'Créez le paiement', 'Depuis votre serveur, avec une Idempotency-Key.')}
{_step(2, 'Redirigez l’acheteur', 'Vers payment_url, puis attendez le webhook.')}
            </ol>
            <p class="dv-keep"><svg aria-hidden="true"><use href="#i-lock"/></svg>Gardez votre clé côté serveur, jamais dans le navigateur.</p>
          </div>
          <div data-reveal>
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

    <section class="pg-sec pg-sec--surf" aria-labelledby="dv-keys-t">
      <div class="wrap">
        <header class="pg-head pg-head--center" data-reveal><p class="kicker">Clés et outils</p><h2 class="h2" id="dv-keys-t">Deux API, chacune son rôle.</h2></header>
        <div class="dv-bento">
          <a class="dv-card" href="docs-paiement.html" data-reveal>
            {icon('wallet')}
            <h3>API Paiement</h3>
            <p>Pour encaisser. Clé du menu Développeur, vérification d’identité requise.</p>
            <p class="dv-key" aria-hidden="true"><span>payments:write</span><code>mp_live_••••8F2k</code></p>
          </a>
          <a class="dv-card" href="docs-produits.html" data-reveal>
            {icon('box', 'ic ic--white')}
            <h3>API Produits</h3>
            <p>Pour lire vos données. Lecture seule, sans vérification d’identité.</p>
            <p class="dv-key dv-key--chips" aria-hidden="true"><span class="dv-chip">Produits</span><span class="dv-chip">Ventes</span><span class="dv-chip">Clients</span><span class="dv-chip">Licences</span></p>
          </a>
          <a class="dv-card" href="docs-paiement.html#test" data-reveal>
            {icon('flask', 'ic ic--white')}
            <h3>Mode test</h3>
            <p>Une clé mp_test_ simule les paiements, sans argent réel.</p>
            <p class="dv-key dv-key--sim" aria-hidden="true"><span class="dv-sim dv-sim--ok">Simuler un paiement réussi</span><span class="dv-sim">Simuler un échec</span></p>
          </a>
          <article class="dv-card dv-card--wide" data-reveal>
            <div>
              {icon('bell', 'ic ic--navy')}
              <h3>Webhooks signés</h3>
              <p>Votre serveur est prévenu de chaque paiement, réussi ou échoué.</p>
              <p class="dv-tags"><span>payment.succeeded</span><span>payment.failed</span><span>HMAC-SHA256</span></p>
            </div>
            <ol class="log dv-log" data-dv-log aria-hidden="true">
              <li><time>10:42:08</time><span>payment.succeeded · 5 000 XOF</span><em>200</em></li>
              <li><time>10:42:31</time><span>payment.succeeded · 14 900 XOF</span><em>200</em></li>
              <li><time>10:43:02</time><span>payment.failed · 2 000 XOF</span><em>200</em></li>
            </ol>
          </article>
        </div>
      </div>
    </section>

    <section class="pg-sec" aria-labelledby="dv-faq-t">
      <div class="wrap">
        <header class="pg-head pg-head--center" data-reveal><p class="kicker">Questions</p><h2 class="h2" id="dv-faq-t">Avant de commencer.</h2></header>
        <div class="dv-faq" data-reveal>
{_q('Faut-il un site codé sur mesure ?', 'Non. Tout site qui peut appeler une API depuis son serveur convient, WordPress compris.')}
{_q('La vérification d’identité est-elle obligatoire ?', 'Oui pour l’API Paiement, qui encaisse de l’argent. Non pour l’API Produits, en lecture seule.')}
{_q('Puis-je tester sans argent réel ?', 'Oui. Avec une clé mp_test_, la page de paiement propose de simuler un paiement réussi ou un échec.')}
{_q('Combien ça coûte ?', 'Aucun abonnement. mepaye prélève 5 % sur chaque paiement encaissé. <a href="tarifs.html">Voir les tarifs</a>.')}
        </div>
      </div>
    </section>
''' + band('Votre première vente par l’API.', 'Créez votre clé et commencez en mode test.', 'Créer ma clé API', 'connexion.html')


# ================================================================== Documentation
def ep(method, path):
    return f'<p class="ep"><span class="ep__m ep__m--{method.lower()}">{method}</span><code>{path}</code></p>'

def tbl(head, rows):
    th = ''.join(f'<th>{h}</th>' for h in head)
    tr = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<div class="tbl"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

def note(t, warn=False):
    return f'<div class="note{" note--warn" if warn else ""}"><span class="ic" aria-hidden="true"><svg><use href="#i-{"lock" if warn else "spark"}"/></svg></span><p>{t}</p></div>'

C = lambda s: f'<code>{s}</code>'

def _dc_card(i, k, method, path, code):
    return (f'            <div class="fxh__card{" is-on" if i == 0 else ""}" data-fxh-s="{i}"><p class="fxh__k">{k}</p>'
            f'<p class="dvh__ep"><span class="ep__m ep__m--{"get" if method in ("GET", "200") else "post"}">{method}</span><code>{path}</code></p>'
            f'<pre class="dvh__pre">{hl(code, "json")}</pre></div>')

DC_ARCH = {
    'docs-paiement.html': ([('Créer', 'POST', '/api/v1/payments', '{\n  "amount": 5000,\n  "currency": "XOF"\n}'),
                            ('Réponse', '200', 'pending', '{\n  "payment_url":\n    "https://pay.mepaye.com/…"\n}'),
                            ('Webhook', 'POST', 'payment.succeeded', '{\n  "status": "PAID",\n  "test": false\n}')], ['Créer', 'Réponse', 'Webhook']),
    'docs-produits.html': ([('Produits', 'GET', '/api/v1/products', '{\n  "name": "Guide Chine",\n  "type": "downloadable"\n}'),
                            ('Ventes', 'GET', '/api/v1/sales', '{\n  "status": "completed",\n  "amount": 25000\n}'),
                            ('Clients', 'GET', '/api/v1/customers', '{\n  "name": "Awa Diop",\n  "country": "BJ"\n}')], ['Produits', 'Ventes', 'Clients']),
}

def docs(slug, title, lead, sections, other, end):
    toc = '\n'.join(f'            <li><a href="#{i}">{t}</a></li>' for i, t, _ in sections)
    secs = '\n'.join(f"""          <section id="{i}">
            <h2>{t}</h2>
{c}
          </section>""" for i, t, c in sections)
    sw = ''.join(f'<a href="{h}"' + (' aria-current="page"' if h == slug else '') + f'>{t}</a>' for h, t in (('docs-paiement.html', 'API Paiement'), ('docs-produits.html', 'API Produits')))
    cards, pills = DC_ARCH[slug]
    arch = ('          <div class="fxh dvh" data-fxh aria-hidden="true">\n' + '\n'.join(_dc_card(i, *c) for i, c in enumerate(cards)) +
            '\n          </div>\n          <ol class="fxh__steps" aria-hidden="true">' + ''.join(f'<li{" class=" + chr(34) + "is-on" + chr(34) if i == 0 else ""}>{x}</li>' for i, x in enumerate(pills)) + '</ol>')
    ctas = f'<nav class="legal-nav dc-sw" aria-label="Documentation">{sw}</nav><a class="link" href="connexion.html">Mes clés API {CHEV}</a>'
    return LOCAL_ICONS + '\n' + ax_hero('code', 'Documentation développeur', title, lead, ctas, arch, 'Exemples de requêtes et de réponses de l’API.') + f"""
    <section class="ax-sec ax-sec--pale dc-sec">
      <div class="wrap legal">
        <nav class="toc" aria-label="Sommaire" data-toc>
          <p>Sommaire</p>
          <ol>
{toc}
          </ol>
          <a class="toc__other" href="{other[0]}">{other[1]} {CHEV}</a>
        </nav>
        <article class="doc dc">
{secs}
          <div class="dc-end">{end}</div>
        </article>
      </div>
    </section>
""" + ax_end('Prêt à intégrer ?', 'Créez votre clé et commencez en mode test.', 'Créer ma clé API', 'connexion.html')

JSON_PAY_RES = '''{
  "id": "cmqz19fk40008jr1hxlyy6065",
  "status": "pending",
  "test": false,
  "payment_url": "https://pay.mepaye.com/checkout/cmqz19fk40008jr1hxlyy6065",
  "externalReference": "CMD-2026-0142",
  "idempotent_replay": false
}'''
CURL_PAY = '''curl -X POST https://mepaye.com/api/v1/payments \\
  -H "Authorization: Bearer mp_live_xxx" \\
  -H "Idempotency-Key: cmd_8f2a1c" \\
  -H "Content-Type: application/json" \\
  -d '{
    "amount": 5000,
    "currency": "XOF",
    "externalReference": "CMD-2026-0142",
    "buyer": {
      "name": "Awa Diop",
      "email": "awa@exemple.com",
      "phone": "+221770000000",
      "country": "SN"
    }
  }\''''
JS_PAY = '''const res = await fetch("https://mepaye.com/api/v1/payments", {
  method: "POST",
  headers: {
    "Authorization": "Bearer " + process.env.MEPAYE_API_KEY,
    "Idempotency-Key": order.id, // votre référence unique
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    amount: 5000,        // minor units (5 000 XOF)
    currency: "XOF",     // = devise de votre boutique
    externalReference: order.id,
    buyer: { name: "Awa Diop", email: "awa@exemple.com", country: "SN" },
  }),
});
const payment = await res.json();
// Redirigez l’acheteur :
redirect(payment.payment_url);'''
HTTP_HOOK = '''POST https://votre-site.com/webhooks/mepaye
X-Mepaye-Event: payment.succeeded
X-Mepaye-Signature: sha256=2f1a…c9
X-Mepaye-Delivery: <id>

{
  "event": "payment.succeeded",
  "data": {
    "id": "cmqz19fk40008jr1hxlyy6065",
    "externalReference": "CMD-2026-0142",
    "status": "PAID",
    "amount": 5000,
    "currency": "XOF",
    "test": false,
    "created_at": "2026-06-29T09:45:30.000Z"
  },
  "deliveredAt": "2026-06-29T09:45:31.200Z"
}'''
NODE_SIG = '''const crypto = require("crypto");

app.post("/webhooks/mepaye", express.raw({ type: "*/*" }), (req, res) => {
  const raw = req.body; // corps brut (non parsé)
  const received = req.header("X-Mepaye-Signature"); // "sha256=..."
  const expected =
    "sha256=" + crypto.createHmac("sha256", process.env.MEPAYE_WEBHOOK_SECRET)
      .update(raw).digest("hex");

  const ok =
    received &&
    crypto.timingSafeEqual(Buffer.from(received), Buffer.from(expected));
  if (!ok) return res.status(401).end();

  const { event, data } = JSON.parse(raw);
  // event = "payment.succeeded" | "payment.failed" ; data.test = mode test
  // → livrez le produit pour data.externalReference
  res.status(200).end(); // répondez vite en 2xx
});'''
PHP_SIG = '''$raw = file_get_contents("php://input");
$received = $_SERVER["HTTP_X_MEPAYE_SIGNATURE"] ?? "";
$expected = "sha256=" . hash_hmac("sha256", $raw, getenv("MEPAYE_WEBHOOK_SECRET"));

if (!hash_equals($expected, $received)) {
  http_response_code(401);
  exit;
}
$payload = json_decode($raw, true);
// $payload["event"], $payload["data"]["externalReference"], $payload["data"]["test"]
http_response_code(200);'''

docs_pay = docs('docs-paiement.html', 'API Paiement',
    'Encaissez depuis votre site ou votre app via pay.mepaye.com. Vous créez un paiement, l’acheteur paie sur notre page hébergée, votre serveur reçoit un webhook signé.',
    [
    ('intro', 'Introduction', f'''            <p>L’API est REST/JSON. URL de base : {C('https://mepaye.com/api/v1')}.</p>
            <ol class="dc-steps">
              <li><b>Créez un paiement</b> ({C('POST /payments')}) : vous recevez une {C('payment_url')}.</li>
              <li><b>Redirigez l’acheteur</b> vers cette adresse, la page hébergée pay.mepaye.com.</li>
              <li><b>L’acheteur paie.</b> Les fonds arrivent dans votre wallet, commission mepaye de 5 %.</li>
              <li><b>Votre serveur reçoit</b> le webhook signé {C('payment.succeeded')} : vous livrez.</li>
            </ol>
            {note('L’acheteur ne voit que pay.mepaye.com. Aucun agrégateur n’est exposé.')}'''),
    ('auth', 'Authentification', f'''            <p>Créez une clé dans le menu <b>Développeur</b>. La vérification d’identité (KYC) est obligatoire. Chaque requête porte l’en-tête :</p>
            {cb(('HTTP', 'http', 'Authorization: Bearer mp_live_xxxxxxxx'))}
            {tbl(['Préfixe', 'Environnement'], [[C('mp_live_'), 'Encaissement réel'], [C('mp_test_'), 'Simulation, voir <a href="#test">Mode test</a>']])}
            <p>La clé porte le scope {C('payments:write')}. Limite : 100 requêtes par minute et par clé.</p>
            {note('Ne l’exposez jamais côté client. Appelez l’API uniquement depuis votre serveur.', warn=True)}'''),
    ('creer', 'Créer un paiement', f'''            {ep('POST', '/api/v1/payments')}
            <p>En-têtes : {C('Authorization')}, {C('Content-Type: application/json')} et {C('Idempotency-Key')}, obligatoire.</p>
            <h3>Corps</h3>
            {tbl(['Champ', 'Description'], [
                [C('amount'), 'Entier, en minor units (5000 = 5 000 XOF). Minimum 100, sans plafond.'],
                [C('currency'), 'La devise de votre boutique.'],
                [C('externalReference'), 'Votre référence de commande, renvoyée dans le webhook.'],
                [C('buyer') + ' <small>optionnel</small>', f'{C("name")}, {C("email")}, {C("phone")}, {C("country")} (ISO-2). Préremplis et modifiables sur la page.']])}
            {cb(('cURL', 'bash', CURL_PAY), ('JavaScript', 'js', JS_PAY))}
            <h3>Réponse</h3>
            {cb(('JSON', 'json', JSON_PAY_RES))}
            <p>Redirigez l’acheteur vers {C('payment_url')}.</p>
            {note(f'<b>Idempotence.</b> Renvoyez la même {C("Idempotency-Key")}, par exemple l’id de votre commande : vous obtenez le même paiement ({C("idempotent_replay: true")}). Jamais de double encaissement, même si vous rejouez la requête.')}'''),
    ('webhooks', 'Webhooks', f'''            <p>Configurez votre URL, votre secret et vos événements dans <b>Développeur › Webhooks</b>. Deux événements, en test comme en live : {C('payment.succeeded')} et {C('payment.failed')}. Le champ {C('test')} du contenu les distingue.</p>
            {cb(('HTTP', 'http', HTTP_HOOK))}
            <p>Nous réessayons jusqu’à 5 fois (délai exponentiel) tant que votre endpoint ne répond pas en 2xx. Après 20 échecs consécutifs, le webhook est désactivé.</p>
            {note(f'Répondez 200 rapidement, et traitez chaque réception de façon idempotente : un même {C("X-Mepaye-Delivery")} peut arriver plus d’une fois.')}'''),
    ('signature', 'Vérifier la signature', f'''            <p>Chaque webhook porte {C('X-Mepaye-Signature: sha256=&lt;hex&gt;')} : un HMAC-SHA256 du corps brut de la requête, avec le secret de votre webhook. Vérifiez-le avant tout traitement, sinon n’importe qui pourrait forger un événement.</p>
            {cb(('Node.js', 'js', NODE_SIG), ('PHP', 'php', PHP_SIG))}
            {note(f'Calculez le HMAC sur le corps brut reçu, sans le re-sérialiser, et comparez en temps constant ({C("timingSafeEqual")} ou {C("hash_equals")}).', warn=True)}'''),
    ('test', 'Mode test', f'''            <p>Une clé {C('mp_test_')} crée un paiement de test : la {C('payment_url')} ouvre une page « Mode test » avec deux boutons, <b>Simuler un paiement réussi</b> et <b>Simuler un échec</b>. Aucun argent réel, aucun agrégateur, vos ventes restent intactes.</p>
            <p>Le webhook correspondant est émis avec {C('test: true')}. Testez votre intégration de bout en bout avant de passer en {C('mp_live_')}.</p>
            <a class="dc-try" href="paiement-test.html"><span class="ic" aria-hidden="true"><svg><use href="#i-flask"/></svg></span><span><b>Voir la page Mode test</b><small>pay.mepaye.com, telle que l’acheteur la voit</small></span>{CHEV}</a>'''),
    ('erreurs', 'Codes d’erreur', f'''            <p>Format : {C('{ "error": { "code", "message" } }')}.</p>
            {tbl(['HTTP', 'Code', 'Signification'], [
                ['401', C('unauthenticated'), 'Clé API manquante ou invalide.'],
                ['403', C('forbidden_scope'), f'La clé n’a pas le scope {C("payments:write")}.'],
                ['403', C('kyc_required'), 'Vérification d’identité requise pour encaisser.'],
                ['400', C('idempotency_key_required'), f'En-tête {C("Idempotency-Key")} manquant.'],
                ['422', C('invalid_body'), 'Corps JSON invalide.'],
                ['422', C('amount_too_low'), 'Montant inférieur au minimum (100 minor units).'],
                ['422', C('currency_mismatch'), 'La devise doit être celle de votre boutique.'],
                ['429', C('rate_limit_exceeded'), 'Plus de 100 requêtes par minute pour cette clé.']])}'''),
    ], ('docs-produits.html', 'Lire vos données ? API Produits'),
    f'<p><b>Prêt ?</b> Créez votre clé dans le menu Développeur et commencez en mode test.</p><a class="btn" href="connexion.html">Créer ma clé {ARROW}</a>')

ENV = '''{
  "message": "success",
  "data": { /* un objet, ou { data: [...], pagination: {...} } pour les listes */ },
  "errors": []
}'''
PAGI = '''{
  "message": "success",
  "data": {
    "data": [ /* … les éléments de la page … */ ],
    "pagination": {
      "next_cursor": "cmp6ljlhl0066jrmw33nbddkz",
      "prev_cursor": null,
      "has_more": true
    }
  },
  "errors": []
}'''
PAGI_SH = '''# Page 1
curl -H "Authorization: Bearer mp_live_xxx" \\
  "https://mepaye.com/api/v1/sales?per_page=50"
# → data.pagination.next_cursor = "cmqxshpz5001ojr40e071659h", has_more = true

# Page suivante : repassez le next_cursor reçu
curl -H "Authorization: Bearer mp_live_xxx" \\
  "https://mepaye.com/api/v1/sales?per_page=50&cursor=cmqxshpz5001ojr40e071659h"
# Bouclez tant que has_more === true.'''
MINOR = '''"current_price": {
  "value": 25000,          // entier en minor units
  "formatted": "25 000 XOF",
  "short": "25000",
  "currency": "XOF"
}
// XOF/XAF/GNF/CDF (0 décimale) : value = unité entière → 25000 = 25 000 FCFA
// EUR/USD (2 décimales) : value = centimes → 2599 = 25,99 €'''
STORE = '''{
  "message": "success",
  "data": {
    "id": "str_cmo9u8zse0001jrof6fhec8rv",
    "name": "Ma Boutique",
    "slug": "ma-boutique",
    "tagline": "Formations & guides",
    "description": null,
    "logo_url": null,
    "favicon_url": null,
    "cover_url": null,
    "url": "https://ma-boutique.mepaye.shop",
    "currency": "XOF",
    "primary_color": "#10B981",
    "seo": { "title": null, "description": null },
    "refund_policy_days": 7,
    "is_verified": true,
    "created_at": "2026-04-22T09:16:29.871Z",
    "updated_at": "2026-06-29T07:37:16.495Z"
  },
  "errors": []
}'''
PRODUCT = '''{
  "id": "cmp6ljlhl0066jrmw33nbddkz",
  "name": "Guide Chine",
  "slug": "guide-chine",
  "type": "downloadable",
  "status": "PUBLISHED",
  "category": { "value": "business_&_entrepreneuriat", "label": "Business & Entrepreneuriat" },
  "is_free": false,
  "pictures": {
    "thumbnail": "/uploads/2026/05/7ec0…IMG_8975.png",
    "cover": "/uploads/2026/05/7ec0…IMG_8975.png"
  },
  "pricing": {
    "type": "one_time",
    "current_price": { "value": 10000, "formatted": "10 000 XOF", "short": "10000", "currency": "XOF" },
    "price": { "value": 10000, "formatted": "10 000 XOF", "short": "10000", "currency": "XOF" }
  },
  "tagline": null,
  "refund_policy_days": 7,
  "created_at": "2026-05-15T07:29:11.817Z",
  "sales_count": 13,
  "reviews_count": 0
}'''
SALE = '''{
  "id": "cmqxshpz5001ojr40e071659h",
  "reference": "MEP-20260628-CB7866",
  "status": "completed",
  "refunded_at": null,
  "original_amount": { "value": 25000, "formatted": "25 000 XOF", "short": "25000", "currency": "XOF" },
  "amount": { "value": 25000, "formatted": "25 000 XOF", "short": "25000", "currency": "XOF" },
  "discount_amount": { "value": 0, "formatted": "0 XOF", "short": "0", "currency": "XOF" },
  "payment": { "amount": { "value": 25000, "currency": "XOF" }, "status": "success", "exchange_rate": 1 },
  "product": { "id": "cmp6l0wf9005jjrmwlztzgtiu", "name": "Guide Chine", "type": "downloadable" },
  "customer": { "id": "cus_YXdhQGV4ZW1wbGUuY29t", "email": "awa@exemple.com", "name": "Awa Diop", "country": "BJ" },
  "discount": null,
  "store": { "id": "cmo9u8zse0001jrof6fhec8rv", "name": "Ma Boutique", "slug": "ma-boutique" },
  "post_purchase": {
    "files": [
      { "id": "cmp6lfy020064jrmwu5phw9yv", "name": "guide.pdf", "size": 419348,
        "download_url": "https://mepaye.com/api/download/eyJmaWxlSWQi…" }
    ],
    "licences": [],
    "instructions": null
  },
  "created_at": "2026-06-28T12:53:10.722Z",
  "paid_at": "2026-06-28T12:55:23.243Z"
}'''
CUSTOMER = '''{
  "id": "cus_YXdhQGV4ZW1wbGUuY29t",
  "name": "Awa Diop",
  "first_name": "Awa",
  "last_name": "Diop",
  "email": "awa@exemple.com",
  "avatar_url": null,
  "phone": { "number": "+221770000000", "country": null },
  "store": {
    "id": "cmo9u8zse0001jrof6fhec8rv",
    "name": "Ma Boutique",
    "logo_url": null,
    "url": "https://ma-boutique.mepaye.shop"
  },
  "created_at": "2026-04-25T17:41:30.610Z",
  "updated_at": "2026-04-25T17:41:30.610Z"
}'''
DISCOUNT = '''{
  "id": "dis_cmqzbw3rk0001jr2i6hl2zyf6",
  "code": "BIENVENUE25",
  "type": "percentage",   // ou "fixed" (montant en minor units)
  "value": 25,            // 25 = -25 % · pour "fixed" : minor units
  "is_active": true,
  "expires_at": null,
  "max_uses": 100,
  "used_count": 3,
  "min_order_xof_cents": null,
  "created_at": "2026-06-29T14:44:00.656Z"
}'''
LICENSE = '''{
  "id": "lic_cmqzbw3rv0003jr2ifk5u3w72",
  "key": "XXXX-YYYY-ZZZZ-1234",
  "status": "available",   // "available" | "used"
  "product": { "id": "cmp6of1fm002cjr3rga7gq3bq", "name": "Mon logiciel", "type": "license" },
  "customer": null,        // { id (cus_*), email, name } une fois attribuée
  "used_at": null,
  "created_at": "2026-06-29T14:44:00.668Z"
}'''
ERR = '''{
  "message": "Forbidden",
  "data": [],
  "errors": ["Cette clé n'a pas le scope requis (products:read)."]
}'''
AUTH2 = 'Authorization: Bearer mp_live_xxxxxxxx\n# ou : X-Api-Key: mp_live_xxxxxxxx'
def curlget(path, key='mp_live_xxx'):
    return f'curl -H "Authorization: Bearer {key}" \\\n  "https://mepaye.com{path}"'
def _get(path, scope, extra):
    return f'{ep("GET", path)}'

docs_prod = docs('docs-produits.html', 'API Produits',
    'Lisez et exportez vos données mepaye vers votre site, votre app ou vos outils : produits, ventes, clients, boutique, codes promo, licences. API REST en lecture seule.',
    [
    ('intro', 'Introduction', f'''            <div class="dc-two">
              <div class="dc-two__c is-on"><p class="dc-two__k">Cette page</p><h3>API Produits</h3><p>Pour <b>lire</b> vos données. Menu Clés API, scopes {C('*:read')}, sans KYC.</p></div>
              <a class="dc-two__c" href="docs-paiement.html"><p class="dc-two__k">Autre API</p><h3>API Paiement</h3><p>Pour <b>encaisser</b> via pay.mepaye.com. Menu Développeur, {C('payments:write')}, KYC requis.</p></a>
            </div>
            <p>URL de base : {C('https://mepaye.com/api/v1')}. Toutes les ressources sont en lecture seule (verbe {C('GET')} uniquement) et limitées à votre boutique : une clé ne voit jamais les données d’une autre boutique.</p>
            <p>Champs en {C('snake_case')}, dates en ISO 8601 UTC, montants en minor units (voir <a href="#format">Format</a>). Si vous gérez plusieurs boutiques, précisez laquelle avec l’en-tête {C('X-Store-Id')}. Le format est aligné sur celui de Chariow.</p>'''),
    ('auth', 'Authentification', f'''            <p>Créez une clé en lecture seule dans le menu <b>Clés API</b>. Aucune vérification d’identité n’est requise. Chaque requête porte l’en-tête :</p>
            {cb(('HTTP', 'http', AUTH2))}
            <p>Chaque clé porte une liste de scopes. Chaque endpoint exige le sien :</p>
            {tbl(['Scope', 'Donne accès à'], [[C('store:read'), 'La boutique'], [C('products:read'), 'Les produits'], [C('sales:read'), 'Les ventes'], [C('customers:read'), 'Les clients'], [C('discounts:read'), 'Les codes promo'], [C('licenses:read'), 'Les clés de licence']])}
            <p>Limite : 100 requêtes par minute et par clé (en-têtes {C('X-RateLimit-Remaining')} et {C('X-RateLimit-Reset')}, puis {C('429')} avec {C('Retry-After')}).</p>
            {note('Gardez la clé côté serveur.', warn=True)}'''),
    ('format', 'Format des réponses', f'''            <p>Chaque réponse est une enveloppe identique :</p>
            {cb(('JSON', 'json', ENV))}
            <h3>Pagination par curseur</h3>
            <p>Les listes renvoient {C('data.data')} (les éléments) et {C('data.pagination')}. Réglez la taille avec {C('per_page')} (20 par défaut, 100 au plus) et avancez avec {C('cursor')}.</p>
            {cb(('JSON', 'json', PAGI), ('Bash', 'bash', PAGI_SH))}
            <p>Sur la dernière page, {C('next_cursor')} vaut {C('null')} et {C('has_more')} vaut {C('false')}.</p>
            <h3>Montants en minor units</h3>
            {note(f'Tous les montants sont des entiers dans la plus petite unité de leur devise : aucune décimale dans {C("value")}, donc aucune erreur d’arrondi. Les champs {C("formatted")} et {C("short")} servent à l’affichage.')}
            {cb(('JSON', 'js', MINOR))}'''),
    ('store', 'Store', f'''            {ep('GET', '/api/v1/store')}
            <p>Le profil de votre boutique. Scope {C('store:read')}. Identifiant préfixé {C('str_')}.</p>
            {cb(('cURL', 'bash', curlget('/api/v1/store', 'mp_live_xxx')), ('Réponse', 'json', STORE))}'''),
    ('products', 'Products', f'''            {ep('GET', '/api/v1/products')}{ep('GET', '/api/v1/products/{id}')}
            <p>Le catalogue. Scope {C('products:read')}. Filtres : {C('search')} (nom), {C('category')}, {C('type')}, {C('per_page')}, {C('cursor')}.</p>
            {cb(('cURL', 'bash', curlget('/api/v1/products?per_page=20', 'mp_live_xxxxxxxx')), ('Réponse', 'json', PRODUCT))}
            <h3>Types de produit</h3>
            {tbl([C('type'), 'Produit'], [[C('downloadable'), 'Ebook, template, fichier téléchargeable'], [C('course'), 'Formation, cours en ligne'], [C('coaching'), 'Coaching, accompagnement'], [C('bundle'), 'Pack de plusieurs produits'], [C('license'), 'Produit à clé de licence'], [C('service'), 'Service, communauté, prestation']])}
            <p>{C('category.value')} est un identifiant indicatif, {C('category.label')} l’intitulé lisible. Le détail {C('/products/{id}')} renvoie le même objet.</p>'''),
    ('sales', 'Sales', f'''            {ep('GET', '/api/v1/sales')}{ep('GET', '/api/v1/sales/{id}')}
            <p>Les commandes, sur tout leur cycle de vie, pas seulement les payées. Scope {C('sales:read')}. Filtres : {C('status')}, {C('customer_id')}, {C('search')}, {C('start_date')}, {C('end_date')} (AAAA-MM-JJ).</p>
            {cb(('cURL', 'bash', curlget('/api/v1/sales?status=completed&per_page=50', 'mp_live_xxx')), ('Réponse', 'json', SALE))}
            <h3>Statuts</h3>
            {tbl([C('status'), 'Signification'], [[C('awaiting_payment'), 'Paiement initié, pas encore confirmé'], [C('completed'), f'Payé, ou remboursé : voir {C("refunded_at")}'], [C('failed'), 'Paiement échoué'], [C('abandoned'), 'Abandonné ou annulé']])}
            {note(f'<b>Téléchargements sécurisés.</b> Pour une vente payée, chaque fichier de {C("post_purchase.files")} porte un {C("download_url")} signé qui expire après environ 24 h, jamais un chemin {C("/uploads")} brut. {C("customer.id")} ({C("cus_*")}) relie la vente aux clients.')}'''),
    ('customers', 'Customers', f'''            {ep('GET', '/api/v1/customers')}{ep('GET', '/api/v1/customers/{id}')}
            <p>Les clients, regroupés par e-mail. Scope {C('customers:read')}. Filtres : {C('search')}, {C('start_date')}, {C('end_date')}.</p>
            {cb(('cURL', 'bash', curlget('/api/v1/customers?search=awa', 'mp_live_xxx')), ('Réponse', 'json', CUSTOMER))}
            <p>Le {C('customer_id')} ({C('cus_*')}) est stable, dérivé de l’e-mail : un même client a le même id dans Sales et Customers. Toutes ses commandes : {C('/api/v1/sales?customer_id=cus_…')}.</p>'''),
    ('discounts', 'Discounts', f'''            {ep('GET', '/api/v1/discounts')}{ep('GET', '/api/v1/discounts/{id}')}
            <p>Les codes promo. Scope {C('discounts:read')}. Filtre : {C('search')} (code). Identifiant préfixé {C('dis_')}.</p>
            {cb(('cURL', 'bash', curlget('/api/v1/discounts', 'mp_live_xxx')), ('Réponse', 'js', DISCOUNT))}
            <p>{C('type: "percentage"')} : {C('value')} est un pourcentage, de 0 à 100. {C('type: "fixed"')} : {C('value')} est un montant en minor units.</p>'''),
    ('licenses', 'Licenses', f'''            {ep('GET', '/api/v1/licenses')}{ep('GET', '/api/v1/licenses/{id}')}
            <p>Les clés de licence de vos produits. Scope {C('licenses:read')}. Filtre : {C('status')} ({C('available')} ou {C('used')}). Identifiant préfixé {C('lic_')}.</p>
            {cb(('cURL', 'bash', curlget('/api/v1/licenses?status=available', 'mp_live_xxx')), ('Réponse', 'js', LICENSE))}
            {note(f'<b>Lecture seule.</b> mepaye livre les clés mais n’est pas un serveur d’activation : aucune route activate, revoke ou activations. {C("status")} passe de {C("available")} à {C("used")} dès qu’une clé est rattachée à une commande.', warn=True)}'''),
    ('erreurs', 'Codes d’erreur', f'''            <p>Même enveloppe en cas d’erreur : {C('message')} est le libellé HTTP, {C('data')} est vide, {C('errors')} contient des messages lisibles.</p>
            {cb(('JSON', 'json', ERR))}
            {tbl(['HTTP', 'Message', 'Signification'], [
                ['401', 'Unauthorised', f'Clé API manquante ou invalide ({C("Authorization")} ou {C("X-Api-Key")}).'],
                ['403', 'Forbidden', f'La clé n’a pas le scope requis, par exemple {C("products:read")}.'],
                ['404', 'Not Found', 'Ressource introuvable, ou hors de votre boutique.'],
                ['429', 'Too Many Requests', f'Plus de 100 requêtes par minute pour cette clé. Voir {C("Retry-After")}.']])}
            <p>Les filtres inconnus sont ignorés plutôt que rejetés.</p>'''),
    ], ('docs-paiement.html', 'Encaisser ? API Paiement'),
    f'<p><b>Prêt ?</b> Créez votre clé en lecture seule dans le menu Clés API.</p><a class="btn" href="connexion.html">Créer ma clé {ARROW}</a>')


# ================================================================== Créer un ebook
STYLES = [('moderne', 'Moderne'), ('luxe', 'Luxe'), ('afrique', 'Afrique'), ('wellness', 'Wellness'), ('business', 'Business'), ('educatif', 'Éducatif')]
CHAPS = ['Pourquoi manger léger', 'Le placard idéal', 'Sept recettes en 20 minutes', 'Tenir sur la durée']
ebook_body = LOCAL_ICONS + '\n' + hero('IA · Propulsé par Claude', 'Votre ebook professionnel, <em>en 10 minutes</em>.',
    'Donnez un sujet, choisissez un style. L’IA écrit, vous regardez les chapitres s’écrire en direct.',
    f'''        <div class="pg-ctas">
          <a class="btn btn--lg" href="inscription.html">Créer mon ebook {ARROW}</a>
          <a class="link" href="tarifs.html">Voir les tarifs {CHEV}</a>
        </div>''') + f'''
    <section class="pg-sec pg-sec--tight" aria-label="Démonstration">
      <div class="wrap">
        <div class="eb" data-eb data-reveal>
          <div class="eb__panel">
            <p class="eb__l">Sujet</p>
            <p class="eb__in">Cuisiner léger au quotidien</p>
            <p class="eb__l" id="eb-style">Style</p>
            <div class="eb__styles" role="radiogroup" aria-labelledby="eb-style">
{chr(10).join(f'              <button type="button" role="radio" aria-checked="{str(i == 0).lower()}" data-eb-style="{k}"{"" if i == 0 else " tabindex=" + chr(34) + "-1" + chr(34)}><i class="eb__sw eb__sw--{k}" aria-hidden="true"></i>{n}</button>' for i, (k, n) in enumerate(STYLES))}
            </div>
            <p class="eb__live"><span class="eb__dot" aria-hidden="true"></span><span data-eb-status>Écriture du chapitre 1</span></p>
          </div>
          <div class="eb__stage" aria-hidden="true">
            <div class="eb__cover eb__cover--moderne" data-eb-cover>
              <i class="eb__arch"></i><i class="eb__motif"></i>
              <span class="eb__tag">Ebook</span>
              <b>Cuisiner léger</b>
              <small>Aïcha K.</small>
            </div>
            <div class="eb__doc">
              <p class="eb__toc">Sommaire</p>
              <ol class="eb__chaps">
{chr(10).join(f'                <li data-eb-ch><span class="eb__n">{i + 1}</span><span class="eb__t">{t}</span><span class="eb__lines"><i></i><i></i><i></i></span></li>' for i, t in enumerate(CHAPS))}
              </ol>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="pg-sec">
      <div class="wrap">
        <div class="eb-f">
          <article class="eb-f__c" data-reveal>{icon('pen')}<h3>Écriture en direct</h3><p>Chaque chapitre s’écrit sous vos yeux, en temps réel.</p></article>
          <article class="eb-f__c" data-reveal>{icon('layout')}<h3>Plus de 15 designs</h3><p>Moderne, luxe, afrique, wellness, business, éducatif…</p></article>
          <article class="eb-f__c" data-reveal>{icon('doc')}<h3>PDF et DOCX</h3><p>Pagination, sommaire, couverture 3D. Modifiable dans Word.</p></article>
        </div>
        <div class="eb-price" data-reveal>
          <p><span class="eb-price__k">1 ebook complet</span><b>50 crédits</b></p>
          <p class="eb-price__s">Le Pack Découverte suffit pour démarrer.</p>
          <a class="link" href="tarifs.html">Voir les packs {CHEV}</a>
        </div>
      </div>
    </section>
''' + band('Votre premier ebook, aujourd’hui.', 'Un sujet suffit pour commencer.', 'Créer mon ebook', 'inscription.html')


# ================================================================== À propos
about_body = LOCAL_ICONS + '\n' + hero('À propos', 'Pourquoi <em>mepaye</em> ?',
    'Des milliers de créateurs africains ont un savoir à partager. La plupart abandonnent avant leur première vente.') + f'''
    <section class="pg-sec pg-sec--tight" aria-labelledby="ab-t">
      <div class="wrap">
        <header class="pg-head pg-head--center" data-reveal><h2 class="h2" id="ab-t">Le talent n’est pas le problème.</h2><p class="lead">Les outils, si. Ils n’ont pas été pensés pour eux.</p></header>
        <div class="ab-vs" data-reveal>
          <div class="ab-vs__c">
            <p class="ab-vs__k">Les outils existants</p>
            <ul>
              <li>{X}Pas de Mobile Money au paiement</li>
              <li>{X}Versements en 72 heures</li>
              <li>{X}Frais cachés</li>
              <li>{X}Interfaces datées</li>
              <li>{X}Support en anglais</li>
            </ul>
          </div>
          <div class="ab-vs__c ab-vs__c--us">
            <p class="ab-vs__k"><img src="assets/brand/logo.svg" alt="mepaye" width="78" height="17"></p>
            <ul>
              <li>{CHECK}Wave, Orange Money, MTN et Moov intégrés</li>
              <li>{CHECK}Versement en moins de 2 heures</li>
              <li>{CHECK}Commission de 5 %, transparente</li>
              <li>{CHECK}L’IA Claude pour créer vos produits</li>
              <li>{CHECK}Zéro abonnement</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="pg-sec pg-sec--surf" aria-label="Notre conviction">
      <div class="wrap">
        <figure class="ab-q" data-reveal>
          <div class="ab-q__img"><img src="assets/img/creatrice.webp" alt="" loading="lazy" decoding="async"></div>
          <div>
            <p class="kicker">Notre conviction</p>
            <blockquote>Un créateur africain ne devrait jamais avoir à choisir entre la qualité des outils occidentaux et l’adaptation locale.</blockquote>
            <p class="ab-q__a">mepaye offre les deux. Une plateforme pensée, conçue et opérée depuis l’Afrique francophone.</p>
          </div>
        </figure>
      </div>
    </section>

    <section class="pg-sec" aria-label="Notre signature">
      <div class="wrap">
        <p class="ab-slogan" data-reveal>Créez. Vendez. <span>mepaye.</span></p>
        <p class="ab-ed" data-reveal>mepaye est édité par OPUXE L.L.C., société de droit américain établie au Nouveau-Mexique : 1209 Mountain Road Pl NE, Ste R, Albuquerque, NM 87110.</p>
      </div>
    </section>
''' + band('Rejoignez mepaye.', 'Votre boutique est prête en quelques minutes.', 'Rejoindre mepaye', 'inscription.html')


# ================================================================== Contact
TOPICS = ['Ma boutique', 'Un paiement', 'Un achat', 'Autre']
contact_body = LOCAL_ICONS + '\n' + hero('Contact', 'Écrivez-nous.', 'Nous lisons chaque message. Réponse en moins de 24 h ouvrées.', plain=True) + f'''
    <section class="pg-sec pg-sec--tight">
      <div class="wrap ct">
        <form class="ct__form" data-ct novalidate data-reveal>
          <fieldset class="ct__topics">
            <legend>Votre message concerne</legend>
            <div>
{chr(10).join(f'              <label><input type="radio" name="sujet" value="{t}"{" checked" if i == 0 else ""}><span>{t}</span></label>' for i, t in enumerate(TOPICS))}
            </div>
          </fieldset>
          <div class="ct__row">
            <label class="ct__f"><span>Nom</span><input name="nom" type="text" autocomplete="name" placeholder="Awa Diop" required></label>
            <label class="ct__f"><span>E-mail</span><input name="email" type="email" autocomplete="email" placeholder="vous@exemple.com" required></label>
          </div>
          <label class="ct__f"><span>Message</span><textarea name="message" rows="5" placeholder="Votre question en quelques lignes. Ajoutez l’adresse de votre boutique si elle est concernée." required></textarea></label>
          <p class="ct__err" data-ct-err role="alert" hidden></p>
          <div class="ct__go">
            <button class="btn" type="submit">Préparer l’e-mail {ARROW}</button>
            <p class="ct__hint">Votre messagerie s’ouvre avec le message prêt à envoyer.</p>
          </div>
        </form>
        <aside class="ct__side">
          <div class="ct__c" data-reveal>{icon('mail')}<h2>Par e-mail</h2><p><a href="mailto:contact@mepaye.com">contact@mepaye.com</a></p><button type="button" class="ct__copy" data-copy-mail="contact@mepaye.com">Copier l’adresse</button></div>
          <a class="ct__c ct__c--link" href="aide.html" data-reveal>{icon('help', 'ic ic--white')}<h2>Centre d’aide</h2><p>Les réponses aux questions fréquentes.</p></a>
          <div class="ct__c" data-reveal>{icon('bell', 'ic ic--white')}<h2>Créateurs connectés</h2><p>Un chat intégré à votre espace arrive bientôt.</p></div>
        </aside>
      </div>
    </section>
'''


# ================================================================== Supprimer mon compte
del_body = LOCAL_ICONS + '\n' + hero('Compte', 'Supprimer mon compte', 'Vous pouvez partir à tout moment. Voici comment, et ce qui se passe ensuite.', plain=True) + f'''
    <section class="pg-sec pg-sec--tight">
      <div class="wrap">
        <div class="dl-ways">
          <article class="dl-w" data-reveal>
            {icon('layout')}
            <h2>Depuis votre espace</h2>
            <ol class="dl-path"><li>Connectez-vous</li><li>Paramètres</li><li>Compte</li><li>Supprimer mon compte</li></ol>
            <a class="link" href="connexion.html">Me connecter {CHEV}</a>
          </article>
          <article class="dl-w" data-reveal>
            {icon('mail', 'ic ic--white')}
            <h2>Sans accès à votre compte</h2>
            <p>Écrivez à support@mepaye.com depuis l’adresse de votre compte, objet « Suppression de compte ». Nous vérifions votre identité, puis enregistrons la demande.</p>
            <a class="link" href="mailto:support@mepaye.com?subject=Suppression%20de%20compte">Écrire au support {CHEV}</a>
          </article>
        </div>

        <div class="dl-tl" data-reveal>
          <h2 class="h3">30 jours pour changer d’avis</h2>
          <ol>
            <li><span class="dl-tl__d">Jour 0</span><b>Demande enregistrée</b><small>Le compte est marqué pour suppression.</small></li>
            <li class="is-mid"><span class="dl-tl__d">Jours 1 à 30</span><b>Vous pouvez annuler</b><small>Reconnectez-vous : un écran propose d’annuler.</small></li>
            <li><span class="dl-tl__d">Jour 30</span><b>Effacement définitif</b><small>Plus rien n’est récupérable.</small></li>
          </ol>
        </div>

        <div class="dl-kd">
          <article class="dl-k" data-reveal>
            <p class="dl-k__h">{icon('trash', 'ic ic--white')}Ce qui est supprimé</p>
            <ul>
              <li>Vos sessions et appareils connus</li>
              <li>Vos notifications et brouillons de génération</li>
              <li>Vos exports de données et jetons d’accès</li>
              <li>Votre nom, e-mail, téléphone et photo, remplacés par une valeur anonyme</li>
            </ul>
          </article>
          <article class="dl-k dl-k--keep" data-reveal>
            <p class="dl-k__h">{icon('shield')}Ce qui est conservé, et pourquoi</p>
            <ul>
              <li><b>Commandes, paiements, ventes et versements.</b> Ce sont des pièces comptables sur de l’argent réellement encaissé.</li>
              <li><b>Les produits achetés par vos clients.</b> Fichiers, formations, communautés et licences restent accessibles à ceux qui les ont payés. Votre boutique affiche « Créateur supprimé » et n’accepte plus de ventes.</li>
            </ul>
          </article>
        </div>
        <p class="ab-ed">mepaye est édité par OPUXE L.L.C., 1209 Mountain Road Pl NE, Ste R, Albuquerque, NM 87110 (États-Unis).</p>
      </div>
    </section>
'''


# ================================================================== 404
nf_body = f'''    <section class="nf">
      <div class="wrap nf__in">
        <div class="nf__door" aria-hidden="true"><span>404</span></div>
        <h1 class="pg-h1">Cette page est introuvable.</h1>
        <p class="lead">Le lien que vous avez suivi ne mène nulle part. Il a peut-être changé, ou la page a été retirée.</p>
        <div class="pg-ctas">
          <a class="btn btn--lg" href="index.html">Retour à l’accueil {ARROW}</a>
          <a class="link" href="aide.html">Centre d’aide {CHEV}</a>
        </div>
      </div>
    </section>
'''

MORE_PAGES = [
    ('developpeurs.html', 'Développeurs', 'L’API Paiement mepaye : encaissez en Mobile Money ou par carte depuis votre propre site, avec une page de paiement hébergée et des webhooks signés.', dev_body, 'developpeurs.html'),
    ('docs-paiement.html', 'API Paiement · Documentation', 'Documentation de l’API Paiement mepaye : créer un paiement, rediriger vers pay.mepaye.com, recevoir et vérifier les webhooks, mode test.', docs_pay, 'developpeurs.html'),
    ('docs-produits.html', 'API Produits · Documentation', 'Documentation de l’API Produits mepaye : lire vos produits, ventes, clients, codes promo et licences, en lecture seule.', docs_prod, 'developpeurs.html'),
    ('creer-ebook.html', 'Créer un ebook avec l’IA', 'Créez un ebook professionnel en 10 minutes avec l’IA Claude : 15 designs, écriture en direct, export PDF et DOCX.', ebook_body, None),
    ('a-propos.html', 'À propos', 'Pourquoi mepaye : une plateforme pensée, conçue et opérée depuis l’Afrique francophone pour les créateurs.', about_body, None),
    ('contact.html', 'Contact', 'Écrivez à l’équipe mepaye : réponse en moins de 24 h ouvrées.', contact_body, None),
    ('supprimer-mon-compte.html', 'Supprimer mon compte', 'Comment supprimer votre compte mepaye, ce qui est effacé et ce qui est conservé.', del_body, None),
    ('404.html', 'Page introuvable', 'Cette page est introuvable.', nf_body, None),
]
