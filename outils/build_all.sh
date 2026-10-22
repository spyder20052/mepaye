#!/bin/sh
# Reconstruit tout le site dans ../site à partir des générateurs Python.
# Usage : sh outils/build_all.sh   (depuis la racine du projet ou d'ailleurs)
set -e
G="$(cd "$(dirname "$0")" && pwd)/generateurs"
SITE="$(cd "$(dirname "$0")/.." && pwd)/site"
cd "$SITE"
# 1. les pages annexes prennent leur pied de page, leur sprite d'icônes et leur bloc téléphone dans l'ANCIENNE accueil
cp "$G/landing-v1/index.html" "$SITE/index.html"
python3 -E "$G/build_pages.py" "$SITE" > /dev/null
python3 -E "$G/build_auth.py" "$SITE" > /dev/null
python3 -E "$G/build_shop.py" "$SITE" > /dev/null
# 2. la NOUVELLE accueil est écrite ensuite
python3 -E "$G/build_landing.py" "$SITE" "$G"
# 3. passes finales : images réactives, liens propres, entrée des pages, versions des CSS/JS
python3 -E "$G/optim.py" "$SITE"
python3 -E "$G/clean_links.py" "$SITE"
python3 -E "$G/enter.py" "$SITE"
python3 -E "$G/bust.py" "$SITE"
echo "site reconstruit dans $SITE"
