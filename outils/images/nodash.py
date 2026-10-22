"""Retire les tirets cadratins (—) et met la ponctuation française qui convient à chaque cas."""
import re, sys, pathlib
D = '—'
def fix(s):
    # 1. libellés d'étape : « Étape 1 — Choisir » → « Étape 1 : Choisir »
    s = re.sub(r'(Étape \d+|Jours? \d+(?: et \d+)?|Modules? \d+(?: à N)?|Module final|Première étape)\s*' + D + r'\s*', r'\1 : ', s)
    # 2. incises encadrées : « … — et comment … — fait » → virgules
    s = re.sub(r'\s' + D + r'\s([^—<>\n]{3,90}?)\s' + D + r'\s', r', \1, ', s)
    # 3. adresses et coordonnées : « Ste R — Albuquerque », « contact@… — réponse », « n° … — constituée »
    s = re.sub(r'(Ste R|mepaye\.com|\d{5,})\s' + D + r'\s', r'\1, ', s)
    # 4. une conjonction ou une précision qui prolonge la phrase → virgule
    s = re.sub(r'\s' + D + r'\s(?=(et|mais|dans|recto|avec|tout est)\b)', ', ', s)
    # 5. en-tête des scripts : « landing v2 — JS natif » → « landing v2 · JS natif »
    s = re.sub(r'\s' + D + r'\s(?=JS natif)', ' · ', s)
    # 6. une explication qui suit → deux-points
    s = re.sub(r'\s' + D + r'\s', ' : ', s)
    # 7. tiret seul servant de valeur d'attente (reçu de paiement)
    s = re.sub(r'>' + D + r'<', '>…<', s)
    return s
n_files = n_before = 0
for p in sys.argv[1:]:
    f = pathlib.Path(p)
    if not f.is_file(): continue
    s = f.read_text()
    if D not in s: continue
    t = fix(s)
    n_before += s.count(D)
    if t != s: f.write_text(t); n_files += 1
    if D in t: print('reste dans', f.name, t.count(D))
print('fichiers corrigés :', n_files, '· tirets avant :', n_before)
