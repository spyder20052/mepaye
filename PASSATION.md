# Passation · site mepaye

Ce document donne à un nouvel assistant tout le contexte du projet. Il permet de relancer le site en local et de continuer le travail sans rien redemander. Lisez-le en entier avant de toucher au code.

*État au 21/10/2026.*

---

## 1. Le projet en bref

| | |
|---|---|
| **Client** | mepaye (marque d'OPUXE L.L.C.) : plateforme de vente de produits digitaux pour créateurs d'Afrique de l'Ouest francophone, paiement en Mobile Money (Wave, Orange Money, MTN, Moov…). 5 % par vente, sans abonnement. |
| **Le site actuel du client** | https://mepaye.com : c'est **la référence** pour les sections, les textes et l'ordre de la page d'accueil (relevé exact dans `reference-mepaye-com.md`). |
| **Notre travail** | Une refonte « premium, façon Apple » du site marketing : la page d'accueil (landing) et 48 pages annexes (fonctionnalités, tarifs, affiliation, développeurs, aide, blog, connexion, boutique de démo, paiement…). |
| **En ligne** | https://landing-mepaye.vercel.app (projet Vercel `landing-mepaye`, équipe `spynels-projects`) |
| **Technique** | Site **statique** (HTML, CSS, JS sans framework), **généré par des scripts Python** dans `outils/generateurs/`. On ne modifie jamais les `.html` de `site/` à la main : ils sont réécrits à chaque construction. |

---

## 2. Relancer le projet en local

**Prérequis :**
- macOS ;
- Python 3.9 ou plus, avec Pillow et NumPy (`pip3 install pillow numpy`) ;
- Node 18 ou plus ;
- Google Chrome installé dans `/Applications`, pour les captures ;
- facultatif : la CLI Vercel (`npx vercel`).

```bash
cd /chemin/vers/Mepaye
sh outils/build_all.sh
```

```bash
python3 outils/serve.py
```

Puis ouvrez http://localhost:5188.

- **Serveur :** `outils/serve.py` (ou `.claude/serve.py` sur le Mac d'origine) reproduit Vercel (adresses sans `.html`, `Cache-Control: no-cache`). Dans Claude Code (application de bureau), il est déclaré dans `.claude/launch.json` sous le nom `mepaye-landing`, à lancer avec l'outil de prévisualisation.
- **Vérification automatique** (49 pages × 2 largeurs : erreurs JS, ressources en 404, débordements) :

```bash
cd outils/captures && npm install && node audit.mjs
```

Le résultat attendu est `49 pages x2 []`. Une liste vide signifie qu'il n'y a aucune erreur.

**Mettre en ligne** : seulement quand l'utilisateur écrit « pousse » (voir § 4).

```bash
cd site && npx -y vercel@latest deploy --prod --yes
```

Il faut être connecté au compte Vercel qui possède le projet `landing-mepaye`. Sur un autre compte, faites `npx vercel login`, puis liez le dossier `site` au projet, ou créez-en un nouveau (le domaine `landing-mepaye.vercel.app` changera alors).

---

## 3. L'arborescence

```text
Mepaye/
├── PASSATION.md              ← ce fichier
├── site/                     ← le site construit (ce qui part sur Vercel)
│   ├── index.html            ← accueil (généré par build_landing.py)
│   ├── landing.css / landing.js   ← styles et scripts de l'accueil
│   ├── styles.css, annex.css, shop.css, auth.css… ← pages annexes
│   ├── vercel.json           ← adresses propres + règles de cache
│   └── assets/
│       ├── app/              ← captures de l'app mepaye (PNG/WebP)
│       ├── people/           ← personnages détourés du hero (acheteur, créatrice, téléphone)
│       ├── scenes/           ← photos de section avec écran de l'app incrusté
│       ├── mockups/          ← mockups iPhone photo-réalistes, écrans incrustés
│       ├── marques/          ← 3 portraits « Plusieurs marques » + cartes boutique
│       ├── focus/            ← encarts nets de l'interface posés sur les photos
│       ├── logos/pm/         ← 12 logos des moyens de paiement
│       ├── brand/            ← logo mepaye, symbole « m », favicons
│       └── r/                ← versions réduites (srcset), générées par optim.py
├── outils/
│   ├── build_all.sh          ← CONSTRUIT TOUT LE SITE (à lancer après chaque modification)
│   ├── generateurs/          ← les scripts Python qui écrivent les pages
│   ├── images/               ← détourage, incrustation d'écrans, nettoyage
│   ├── captures/             ← scripts Playwright (audit, captures de sections)
│   └── barre-ios/            ← barre d'état iOS et bannière de notification de référence
├── captures-app/             ← captures brutes de l'app ; enjolivees/ = versions au contenu vendeur
├── photos-a-trier/           ← images générées par l'utilisateur (sources des visuels)
├── captures-revue/           ← captures envoyées à l'utilisateur pour validation
├── reference-mepaye-com.md   ← textes exacts de mepaye.com, section par section
├── prompts-*.md, prompt-couverture-ebook.md, campagne-photo.md ← prompts de génération d'images
└── etude-polices/            ← étude de typographie (choix : Urbanist + Inter)
```

### L'ordre de construction (`outils/build_all.sh`)

1. **Base des pages annexes :** copie de l'**ancienne** accueil (`generateurs/landing-v1/index.html`) dans `site/index.html`. Les pages annexes y puisent leur pied de page, leur sprite d'icônes et leur bloc téléphone. **Ne supprimez pas `landing-v1`.**
2. **Pages annexes :** `build_pages.py`, qui exécute aussi `fx_page.py`, `tarifs_page.py`, `more_pages.py`, `aff_page.py`, `dev_page2.py`, `ebook_page.py`, `secondary_pages.py`, `hc_page.py` et `blog_page.py`, puis `build_auth.py` et `build_shop.py`.
3. **Nouvelle accueil :** `build_landing.py` écrit l'accueil par-dessus. **C'est le fichier qui contient toutes les sections de l'accueil.**
4. **Images réactives :** `optim.py` crée les versions réduites (`assets/r/`), ajoute `srcset` et `sizes`, et met le téléphone du hero en priorité de chargement.
5. **Liens propres :** `clean_links.py` écrit `/tarifs` et non `tarifs.html`.
6. **Entrée des pages :** `enter.py` ajoute l'apparition progressive sur les pages annexes et rend le chargement des polices non bloquant.
7. **Versions :** `bust.py` ajoute `?v=empreinte` aux CSS et JS, pour qu'aucun ancien fichier ne reste en cache.

### Où modifier quoi

| Je veux changer… | Fichier |
|---|---|
| un texte, l'ordre ou le contenu d'une section de l'accueil | `outils/generateurs/build_landing.py` |
| le style de l'accueil | `site/landing.css` (règles ajoutées par blocs commentés, **les dernières règles gagnent**) |
| l'animation du « m », la barre qui se cache, l'apparition au défilement | `site/landing.js` |
| une page annexe | `outils/generateurs/build_pages.py` et les `*_page.py` |
| la boutique de démo et le paiement | `build_shop_base.py` / `build_shop_pages.py` (concaténés dans `build_shop.py`) |
| connexion et inscription | `build_auth.py` |

---

## 4. Les règles de l'utilisateur (à respecter absolument)

1. **Ne jamais mettre en ligne sans « pousse » explicite.**
   - Travaillez en local, montrez des captures, puis attendez la demande.
   - Une demande vaut pour un seul envoi.
   - Le 21/10/2026, un déploiement non demandé a dû être annulé.
2. **Langue :**
   - tout est en **français**, accents compris ;
   - **jamais de tiret cadratin « — »**, ni dans le site, ni dans les messages : remplacez-le par des deux-points, des virgules ou « : » ;
   - après chaque construction, vérifiez avec `grep -c "—" site/index.html`, qui doit renvoyer 0.
3. **Peu de texte.** Le client « ne veut vraiment pas beaucoup de texte » :
   - des phrases courtes ;
   - des puces de 2 à 4 mots ;
   - une accroche d'une ligne.
4. **Ne pas réécrire les textes de mepaye.com sans demande.**
   - Les textes de l'accueil sont ceux de `reference-mepaye-com.md`.
   - Quand l'utilisateur demande un changement de mise en page, ne touchez pas aux textes : il l'a reproché le 21/10/2026.
5. **Style « Apple » :** premium, épuré, centré, beaucoup d'air, boutons pilule sobres (bleu plein, et contour bleu). **Toutes les sections de l'accueil restent centrées.** Une mise en page « texte à gauche, image à droite » a été refusée.
6. **Typographie :** Urbanist pour les titres, en medium (500) ; Inter pour le texte, en 400. Le client refuse le gras épais.
7. **Illustrations :**
   - de **vraies captures de l'app**, sans données inventées dans le contenant ;
   - on peut enjoliver le **contenu** (soldes, ventes, noms), jamais le **contenant** (l'interface) ;
   - on ne modifie **jamais** le design ni la structure d'un écran capturé : on peut seulement remplacer des images et corriger un petit défaut visuel ; en voyant un mockup, on doit reconnaître la vraie interface de l'app (rappel du client, 22/10/2026) ;
   - pas de photos de banque d'images : les personnes viennent des images générées par l'utilisateur ;
   - les écrans doivent être **nets et lisibles**.
8. **Notifications :** reprendre le format exact de l'app, une bannière iOS avec :
   - l'icône « m » bleue sur fond blanc ;
   - « **Une vente ! Mepaye te paye 🎉** » en gras, avec « maintenant » à droite ;
   - « Tu viens de vendre pour 3 500 XOF » en dessous.
9. **Barre d'état des téléphones :** la vraie barre iOS (SF Pro, 9:41, mesures Apple). Une barre « dessinée » a été refusée.
10. **Arches :** les arches décoratives sont **toujours entières**, jamais rognées dans un coin.
11. **Adresses propres :** jamais de `.html` dans les liens.
12. **Mobile d'abord :**
    - le site est surtout vu sur téléphone ;
    - le hero doit tenir **entièrement** dans l'écran visible, centré verticalement, de 360 à 430 px de large ;
    - vérifiez chaque modification sur ordinateur **et** à 390 px.
13. **Mouvement :** discret et premium.
    - **aucune animation dans le hero** ;
    - une apparition douce au défilement pour les autres sections ;
    - les avis défilent en continu, avec un fondu sur les bords ;
    - l'animation du « m » avant le pied de page reste plate, jamais en 3D ;
    - tout s'arrête si le mouvement réduit est activé.
14. **Rien n'est annoncé comme fini sans capture** : ordinateur et 390 px.
15. **Sécurité :**
    - ne saisissez jamais de mot de passe ;
    - pour capturer l'app (https://mepaye.com/app), c'est l'utilisateur qui se connecte lui-même dans le navigateur intégré ;
    - les modifications de texte faites dans l'app pour les captures restent locales à l'onglet et ne touchent jamais le compte.

---

## 5. La page d'accueil, section par section (état actuel)

L'ordre et les textes sont ceux de mepaye.com.

| # | Section | Visuel actuel |
|---|---|---|
| 1 | **Hero** : « Créez. Vendez. Encaissez. » (une ligne), phrase d'accroche, boutons « Commencer » / « Se connecter », « Sans abonnement. 5 % par vente, c'est tout. » (sous les boutons sur ordinateur, sous l'image sur téléphone) | Scène dans une arche bleu pâle : iPhone photo-réaliste détouré (page produit de Studio Aïcha) au centre, acheteur assis à gauche (masqué sur téléphone), créatrice debout à droite, petite bannière de notification posée sur l'image |
| 2 | Votre boutique, à votre image. | Mockup : deux iPhone flottants (liste des produits, page produit) |
| 3 | Le paiement, sous toutes ses formes. | Gros plan iPhone avec la notification, puis la grille des 12 logos |
| 4 | Une identité. Plusieurs marques. | Trois arches avec trois créateurs (Studio Aïcha, Wellness Pro, Digital Habit), chacun montrant sa boutique, et une carte lisible dessous ; défilement horizontal sur téléphone |
| 5 | Votre argent, sur votre Mobile Money. | Photo d'une créatrice qui montre son solde, avec l'encart « Solde disponible » |
| 6 | Décrivez votre idée. Mepaye rédige. | Main tenant un iPhone, avec le formulaire de génération d'ebook par l'IA, sur fond bleu pâle |
| 7 | Un seul endroit. Tous vos produits. | Grille de 9 types de produits |
| 8 | **API Paiement** : « Gardez votre site. Mepaye encaisse. » (remplace « Une boutique à votre image. », doublon de la section 2, à la demande du client le 22/10/2026) | iPhone posé à plat (`mockups/paiement.webp`) avec la vraie page de paiement hébergée `pay.mepaye.com` (ebook à 3 500 XOF, Studio Aïcha), encart net des moyens de paiement (`focus/paiement.webp`), puces « Clé API » et « Mode test » |
| 9 | Vos clients deviennent vos vendeurs. | Deux amies et l'écran d'affiliation, avec l'encart du niveau Argent |
| 10 | Chaque décision, appuyée par vos chiffres. | Doigt sur la courbe des revenus, avec l'encart de la courbe |
| 11 | Ils l'utilisent. Ils l'adorent. | Avis en bande infinie, de droite à gauche, avec fondu sur les bords et pause au survol |
| 12 | Pourquoi Mepaye. | 4 cartes |
| 13 | Commencez aujourd'hui. | Animation du « m » formé par deux personnes (logo plat) |
| 14 | Pied de page | Comme mepaye.com |

### L'ebook de démonstration

Le produit mis en avant partout est « **Ebook : créer et vendre des produits numériques** », à 3 500 XOF, dans la boutique « Studio Aïcha ». Sa couverture est `photos-a-trier/couverture-ebook-2.webp`. Les captures de l'app qui le montrent sont dans `captures-app/enjolivees/` (`produit-couv.png`, `produits.png`).

### Couleurs et repères

| Rôle | Valeur |
|---|---|
| Bleu de la marque | `#0866FF` |
| Encre | `#18181B` |
| Texte | `#3F3F46` |
| Gris | `#71717A` |
| Panneaux bleu pâle | `#EAF4FE` / `#EFF6FF` |
| Panneaux gris | `#F4F4F5` |
| Marine (photos) | `#10244A` |

Rayons : panneaux 24 px, cartes 16 à 22 px, boutons en pilule.

---

## 6. Comment on fabrique les visuels (la chaîne d'images)

Toutes les images de personnes et de téléphones sont **générées par l'utilisateur** à partir des prompts des fichiers `prompts-*.md`, avec un **écran vert uni `#00FF00`**. On y incruste ensuite les vraies interfaces.

1. **Capturer l'interface.**
   - Dans le navigateur intégré, réglé à 400 × 860 (dpr 2), l'utilisateur étant connecté, ouvrez la page de l'app ou de la boutique `atelier-demo.mepaye.shop`.
   - Modifiez le **contenu** en JS dans l'onglet : noms, montants, « Atelier Démo » remplacé par « Studio Aïcha », bandeau cookies masqué.
   - Capturez en **PNG sans perte** (action `zoom` sur toute la page), jamais en JPEG.
   - Les images extérieures ne se chargent pas dans la boutique : collez les couvertures après coup, avec Pillow.
2. **Incruster dans une photo à un téléphone :** `outils/images/greenscreen.py`.

```bash
UP=3 python3 outils/images/greenscreen.py photo.webp ecran.png sortie.png <dynamic_island 0|1> <hauteur_barre_onglets_px>
```

   - Il retrouve les 4 coins de l'écran vert (RANSAC, insensible aux doigts) et pose l'écran en perspective à 3 fois la résolution.
   - Il ajoute la vraie barre d'état iOS (`outils/barre-ios/sb-0.png` et `sb-1.png`) et la barre d'accueil.
   - Il retire le liseré vert autour des doigts.
   - Pour un téléphone vu très en biais (posé à plat), ajoutez `RATIO=852/393` : le format apparent de l'écran est faussé par la perspective, cette option impose le vrai format.
   - La page de paiement se capture sans compte : achat test dans la boutique démo (cookie `preferred-currency=XOF`, faux nom, pays Côte d'Ivoire, numéro fictif), arrêt sur `pay.mepaye.com` sans payer.
3. **Incruster dans un mockup à plusieurs téléphones :** `outils/images/mockup.py`.

```bash
UP=1.5 python3 outils/images/mockup.py mockup.png sortie.png ecran1.png[:barre_onglets[:cote_cache]] ecran2.png …
```

   - Les écrans sont attribués de gauche à droite.
   - Indiquez `:0:r` pour un écran caché à droite par un autre téléphone, `:0:b` pour un écran coupé par le bas.
4. **Détourer une personne ou un téléphone sur fond blanc :**
   - masque de base par la vision macOS : `outils/images/cutout` (à recompiler depuis `cutout.swift` avec `swiftc`) ;
   - finition : `outils/images/cutwhite.py`, avec l'option `hair` pour les tresses ;
   - autre outil : `defringe.py`.
5. **Notification iOS :** rendue en HTML avec SF Pro (`outils/barre-ios/notif.html`), capturée par `outils/captures/notifscr.mjs`.
6. **Export :** WebP qualité 84 à 90, dans le bon dossier de `site/assets/`. Reconstruisez ensuite : `optim.py` fabrique les versions réduites.

**Contrôle qualité avant de livrer :**
- zoomez sur chaque écran incrusté : texte lisible, aucun liseré vert, coins alignés ;
- vérifiez chaque détourage sur un fond coloré.

---

## 7. Captures et vérifications

Les scripts sont dans `outils/captures/` (Playwright avec le Chrome du système) :

| Script | Rôle |
|---|---|
| `audit.mjs` | contrôle les 49 pages à deux largeurs |
| `sec.mjs <dossier> <idSection>` | capture une section sur ordinateur (`-d.png`) et à 390 px (`-m.png`) |
| `herocenter.mjs` / `heromob.mjs` | vérifient que le hero tient dans l'écran du téléphone, à 360, 390 et 430 px |
| `herosizes.mjs` | hero à 1000, 1280 et 1440 px de large |
| `weight.mjs` | poids des images chargées (premier écran et page entière) |

Plusieurs scripts écrivent leurs captures dans un dossier passé en argument. Remplacez les anciens chemins de dossier temporaire par un dossier du projet, par exemple `captures-revue/`.

**Performances actuelles :**
- environ 100 Ko d'images au premier écran ;
- environ 0,9 Mo pour toute la page sur téléphone, 0,7 Mo sur ordinateur.

Le cache Vercel est réglé dans `site/vercel.json` : `assets/r/` est immuable pendant 1 an, le reste des `assets` est gardé 1 jour.

---

## 8. Ce qui reste à faire ou à valider

1. **Le hero n'est pas encore validé par le client.** Dernières demandes de l'utilisateur :
   - titre sur une ligne ;
   - boutons façon Apple ;
   - textes d'origine conservés ;
   - notification réduite et posée sur l'image ;
   - tout tient dans l'écran du téléphone.

   À montrer et à faire valider.
2. **Boutons du hero :** « Commencer gratuitement → » a été raccourci en « Commencer ». C'est à confirmer avec l'utilisateur : les textes d'origine ne doivent pas changer sans accord.
3. **Revue section par section** : la revue de chaque section de l'accueil, dans l'ordre de la page, est en cours. Améliorez le visuel sans casser la structure centrée ni les textes.
4. **Responsive :** continuer l'optimisation mobile au-delà du hero. C'est la priorité du client.
5. **Pages annexes :** elles utilisent encore l'ancienne direction artistique (Parkinsans + Geist, voir `annex.css`). L'accueil est passée à Urbanist + Inter. Une harmonisation sera à proposer, **sans la faire sans accord**.
6. **Mockup « à plat »** (`site/assets/mockups/plat.webp`) : prêt, mais pas encore utilisé. Il est réservé aux pages annexes.

---

## 9. Historique utile (pour comprendre les choix)

- **19/10/2026 :** dernière version de l'ancienne direction (Parkinsans + Geist, campagne photo « La porte »). Déploiement Vercel `enyqg6jm3`, à garder comme point de retour.
- **20/10/2026 :** brief du client : refaire l'accueil à partir de mepaye.com (mêmes sections, mêmes textes), en plus premium, avec de vraies captures de l'app, sans 3D, et l'animation du « m » seulement avant le pied de page.
- **21/10/2026 :**
  - étude typographique, choix d'Urbanist + Inter ;
  - mockups photo-réalistes générés par l'utilisateur ;
  - section « Plusieurs marques » avec trois portraits ;
  - avis en défilement infini ;
  - hero mobile tenant dans un écran ;
  - notification au format de l'app ;
  - nouvel ebook ;
  - optimisation des images ;
  - plusieurs mises en ligne demandées par l'utilisateur.
- **Refusé par l'utilisateur** (à ne pas reproposer) :
  - photos de banque d'images ;
  - dégradés agressifs ;
  - texte en gras ;
  - mise en page texte et image côte à côte ;
  - notification en large bandeau ;
  - barre d'état iOS dessinée à la main ;
  - fond jaune dans la section Création ;
  - porte qui s'ouvre au chargement (elle existe déjà sur la page de connexion) ;
  - trois téléphones de face pour « Plusieurs marques ».
