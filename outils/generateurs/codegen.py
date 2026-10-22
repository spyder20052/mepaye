"""Coloration du code et blocs de code partagés (accueil, Développeurs, documentation)."""
import re, html as _h

_TOK = re.compile(
    r'(?P<c>(?<![:\w])//[^\n]*|(?:(?<=\s)|^)#[^\n]*)'
    r'|(?P<s>"(?:[^"\\\n]|\\.)*"|\'(?:[^\'\\\n]|\\.)*\'|`[^`\n]*`)'
    r'|(?P<n>(?<![\w-])\d+(?:\.\d+)?(?![\w-]))'
    r'|(?P<k>\b(?:const|let|await|async|return|if|require|function|true|false|null|new|exit)\b)'
    r'|(?P<f>\b[A-Za-z_]\w*(?=\())', re.M)

def hl(code, lang='js'):
    out, i = [], 0
    hash_ok = lang in ('bash', 'http', 'curl')
    for m in _TOK.finditer(code):
        kind = m.lastgroup
        if kind == 'c' and m.group(0).startswith('#') and not hash_ok:
            continue
        if kind == 's' and lang == 'json' and re.match(r'\s*:', code[m.end():]):
            kind = 'k'
        out.append(_h.escape(code[i:m.start()], quote=False))
        out.append(f'<span class="{kind}">{_h.escape(m.group(0), quote=False)}</span>')
        i = m.end()
    out.append(_h.escape(code[i:], quote=False))
    return ''.join(out)

def lines(spec, lang):
    """spec : liste de (étape ou None, texte). Rend des lignes numérotées pour la fenêtre de code."""
    res = []
    for l, t in spec:
        body = hl(t, lang) if t else ' '
        res.append(f'<span class="ln"{f" data-l={chr(34)}{l}{chr(34)}" if l is not None else ""}>{body}</span>')
    return '\n'.join(res)

def snippets(amount=5000):
    """Les trois exemples « créer un paiement » de l'API Paiement réelle."""
    js = [
        (0, '// 1. Votre clé, créée dans le menu Développeur'),
        (0, 'const key = process.env.MEPAYE_API_KEY;'),
        (None, ''),
        (1, '// 2. Créer le paiement'),
        (1, 'const res = await fetch("https://mepaye.com/api/v1/payments", {'),
        (1, '  method: "POST",'),
        (1, '  headers: {'),
        (0, '    "Authorization": `Bearer ${key}`,'),
        (1, '    "Idempotency-Key": order.id,'),
        (1, '    "Content-Type": "application/json",'),
        (1, '  },'),
        (1, '  body: JSON.stringify({'),
        (1, f'    amount: {amount},'),
        (1, '    currency: "XOF",'),
        (1, '    externalReference: order.id,'),
        (1, '  }),'),
        (1, '});'),
        (None, ''),
        (2, '// 3. Rediriger l’acheteur vers la page de paiement'),
        (2, 'const { payment_url } = await res.json();'),
        (2, 'redirect(payment_url);'),
    ]
    php = [
        (0, '// 1. Votre clé, créée dans le menu Développeur'),
        (0, '$key = getenv("MEPAYE_API_KEY");'),
        (None, ''),
        (1, '// 2. Créer le paiement'),
        (1, '$res = wp_remote_post("https://mepaye.com/api/v1/payments", ['),
        (1, '  "headers" => ['),
        (0, '    "Authorization"   => "Bearer " . $key,'),
        (1, '    "Idempotency-Key" => $order_id,'),
        (1, '    "Content-Type"    => "application/json",'),
        (1, '  ],'),
        (1, '  "body" => wp_json_encode(['),
        (1, f'    "amount"            => {amount},'),
        (1, '    "currency"          => "XOF",'),
        (1, '    "externalReference" => $order_id,'),
        (1, '  ]),'),
        (1, ']);'),
        (None, ''),
        (2, '// 3. Rediriger l’acheteur vers la page de paiement'),
        (2, '$payment = json_decode(wp_remote_retrieve_body($res));'),
        (2, 'wp_redirect($payment->payment_url);'),
    ]
    curl = [
        (0, '# 1. Votre clé, créée dans le menu Développeur'),
        (1, 'curl -X POST https://mepaye.com/api/v1/payments \\'),
        (0, '  -H "Authorization: Bearer $MEPAYE_API_KEY" \\'),
        (1, '  -H "Idempotency-Key: cmd_8f2a1c" \\'),
        (1, '  -H "Content-Type: application/json" \\'),
        (1, '  -d \'{'),
        (1, f'    "amount": {amount},'),
        (1, '    "currency": "XOF",'),
        (1, '    "externalReference": "CMD-0142"'),
        (1, '  }\''),
        (None, ''),
        (2, '# 2. Redirigez l’acheteur vers payment_url'),
        (2, '# 3. Livrez à la réception du webhook payment.succeeded'),
    ]
    return (f'<pre class="dw__code" data-code="js"><code>{lines(js, "js")}</code></pre>\n'
            f'<pre class="dw__code" data-code="php" hidden><code>{lines(php, "php")}</code></pre>\n'
            f'<pre class="dw__code" data-code="curl" hidden><code>{lines(curl, "bash")}</code></pre>')

_n = [0]
def cb(*tabs):
    """Bloc de code de la documentation. tabs : (étiquette, langage, code)."""
    _n[0] += 1
    k = _n[0]
    if len(tabs) == 1:
        head = f'<span class="cb__lang">{tabs[0][0]}</span>'
    else:
        head = '<div class="cb__tabs" role="tablist" aria-label="Langage">' + ''.join(
            f'<button role="tab" type="button" id="cb{k}t{i}" aria-controls="cb{k}p{i}" aria-selected="{str(i == 0).lower()}"{"" if i == 0 else " tabindex=" + chr(34) + "-1" + chr(34)}>{t[0]}</button>'
            for i, t in enumerate(tabs)) + '</div>'
    pres = ''.join(
        f'<pre class="cb__pre" id="cb{k}p{i}"' + (f' role="tabpanel" aria-labelledby="cb{k}t{i}"' if len(tabs) > 1 else '') + (' hidden' if i else '') + f'><code>{hl(t[2].strip(chr(10)), t[1])}</code></pre>'
        for i, t in enumerate(tabs))
    return (f'<div class="cb" data-cb><div class="cb__bar">{head}'
            '<button type="button" class="cb__copy" data-cb-copy aria-label="Copier le code"><svg class="ic-copy" aria-hidden="true"><use href="#i-copy"/></svg><svg class="ic-ok" aria-hidden="true"><use href="#i-check"/></svg></button></div>'
            f'{pres}</div>')
