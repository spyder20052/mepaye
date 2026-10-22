# Miniatures des produits de Studio Aïcha · prompts

Ces six miniatures remplacent les couvertures à plat (fonds vert et marine avec une icône) dans la liste des produits, dans le mockup « Votre boutique » et dans la boutique de démo. Elles suivent exactement la construction de la couverture déjà faite, « Créer et vendre des produits numériques » (`prompt-couverture-ebook.md`), pour qu'on les voie comme une collection.

| # | Produit | Type | Prix | Statut |
|---|---|---|---|---|
| 0 | Ebook : créer et vendre des produits numériques | Ebook | 3 500 XOF | **fait** (référence) |
| 1 | Modèle de facture pour freelance | Template | 2 000 XOF | à générer (visible dans le mockup) |
| 2 | Guide : lancer sa boutique en ligne | Ebook | 5 000 XOF | à générer (visible dans le mockup) |
| 3 | Calendrier éditorial trimestriel | Template | 4 500 XOF | à générer (visible dans le mockup) |
| 4 | Formation courte : vendre en ligne | Formation | 25 000 XOF | à générer |
| 5 | Formation : tenir sa comptabilité de freelance | Formation | 15 000 XOF | à générer |
| 6 | Pack de 30 modèles de publications | Template | 7 500 XOF | à générer |

**Priorité :** 1, 2 et 3, les trois visibles dans le mockup de la boutique sur l'accueil.

---

## 1. La règle de la collection (ce qui ne change jamais)

Chaque miniature a la même construction que la couverture de l'ebook :

```text
┌──────────────────────────────┐
│ PASTILLE                     │  ← type du produit (je la pose)
│ Titre                        │  ← 2 ou 3 lignes (je le pose)
│ du produit                   │
│                   ┌──────┐   │
│        objet      │ app  │   │  ← l'écran : une vraie page mepaye
│         ▟▀▀▀▙     │      │   │
│         ▌   ▐     └──────┘   │  ← le même socle en arche cobalt
└──────────────────────────────┘
```

1. **Le même décor :** fond bleu pâle `#EDF4FF`, lumière de fenêtre venant de la gauche, avec les mêmes ombres douces en diagonale.
2. **Le même socle :** l'arche cobalt `#0866FF`, toujours en bas à droite, toujours de la même taille.
3. **Le même téléphone :** iPhone dans une coque cobalt mate, écran en vert chroma. J'y incruste une **vraie page de l'app** : c'est elle qui met mepaye en avant sur chaque miniature.
4. **Un seul objet par produit,** pour raconter le sujet en un coup d'œil, dans les couleurs de la collection : blanc cassé, cobalt, marine `#10244A`, bleu pâle.
5. **Un rythme dans la grille :** les miniatures paires ont une main (comme la référence), les impaires montrent le téléphone posé seul sur le socle. Vue en liste, la boutique alterne sans se répéter.
6. **Le tiers haut gauche reste vide** (45 % de l'image) : j'y pose la pastille et le titre en Urbanist medium marine, nets et identiques d'une miniature à l'autre.
7. **Aucun texte généré dans l'image.**

### Le conseil qui fait la cohérence

Générez les six dans **la même conversation** de votre outil, en joignant à chaque fois la couverture déjà faite (`couverture-ebook-2.png`) comme **image de référence de style**. Ajoutez au début du prompt : `Match the exact lighting, backdrop color, pedestal, phone case and camera of the reference image.`

### Le bloc de style (à coller à la fin de chaque prompt)

```text
Square 1:1 premium product cover scene, part of a consistent series, Apple-style minimal product photography. Seamless pale blue #EDF4FF studio backdrop. A smooth matte cobalt blue #0866FF pedestal shaped like a rounded arch stands in the lower right of the frame, always the same size and position. The phone is a modern iPhone in a matte cobalt blue #0866FF case; its screen is a perfectly flat uniform chroma green #00FF00 from edge to edge, no reflection, no interface, all four rounded screen corners fully visible and unobstructed. Soft window light from the left casting gentle diagonal window shadows on the backdrop, soft natural contact shadows. True real-world scale for every object: the phone is 150 mm tall, the pedestal about 120 mm tall. The whole top-left 45 percent of the frame is empty pale blue backdrop, reserved for a title. Color world strictly cobalt blue, navy #10244A, pale blue, off-white and natural skin tones. Shot on a Hasselblad, 80mm, f/5.6, everything tack sharp, clean whites, subtle film grain, no HDR, photographic realism.
```

### À exclure (pour toutes)

```text
text, letters, numbers, logos, watermark, user interface on screen, screen reflection, oversized phone, tiny hand, extra or fused fingers, distorted hands, waxy or plastic skin, cluttered background, more than one prop, props in other colors, warm orange cast, green, purple, oversaturated, harsh shadows, wide-angle distortion, CGI look, 3D render look
```

---

## 2. Les six scènes

Chaque prompt ci-dessous décrit seulement la scène. Collez ensuite le bloc de style.
**Fichier :** `photos-a-trier/miniature-<numéro>.png`, carré, 2 048 × 2 048 px minimum.

### 1 · Modèle de facture pour freelance
- **Pastille :** `TEMPLATE` · **Titre :** « Facture / pour freelance »
- **Écran incrusté :** la page produit du modèle dans la boutique Studio Aïcha, avec la notification « Une vente ! Mepaye te paye ».

```text
The phone stands alone, upright, leaning back slightly against the arch pedestal, screen facing the camera. In front of the pedestal, a single crisp sheet of off-white A5 paper lies flat on the floor at a slight angle, like a printed invoice: a thin cobalt band at the top and a few faint grey lines, no readable text or numbers.
```

### 2 · Guide : lancer sa boutique en ligne
- **Pastille :** `EBOOK` · **Titre :** « Lancer sa / boutique / en ligne »
- **Écran incrusté :** l'accueil de la boutique Studio Aïcha avec ses produits.

```text
A dark-skinned hand with short clean natural nails holds the phone upright from the right side, its bottom edge resting on the arch pedestal, the phone turned slightly toward the camera. The hand is at true adult scale: the phone is slightly narrower than the palm, only the thumb and two fingertips overlap the side frame. Beside the pedestal on the left stands a small off-white paper shopping bag with cobalt rope handles, about 15 cm tall, plain, no print.
```

### 3 · Calendrier éditorial trimestriel
- **Pastille :** `TEMPLATE` · **Titre :** « Calendrier / éditorial / trimestriel »
- **Écran incrusté :** la page produit du calendrier dans la boutique.

```text
The phone stands alone, upright, leaning back slightly against the arch pedestal, screen facing the camera. To the left of the pedestal stands a small off-white desk tent calendar with a navy wire binding, about 12 cm wide, its page showing only a simple grid of empty squares with three squares filled in cobalt, no numbers, no text.
```

### 4 · Formation courte : vendre en ligne
- **Pastille :** `FORMATION` · **Titre :** « Vendre / en ligne »
- **Écran incrusté :** la page produit de la formation (vidéo et liste des quatre modules).

```text
A dark-skinned hand with short clean natural nails holds the phone horizontally in landscape orientation, resting its lower edge on top of the arch pedestal, as if showing a video lesson to the camera. True adult scale: the phone's width is about the length of the hand's fingers, the thumb rests on the bottom frame without touching the screen. Behind the pedestal, slightly out of focus, a pair of small white wireless earbuds in their open white case.
```

### 5 · Formation : tenir sa comptabilité de freelance
- **Pastille :** `FORMATION` · **Titre :** « Tenir sa / comptabilité / de freelance »
- **Écran incrusté :** le portefeuille mepaye (solde disponible et dernières ventes).

```text
The phone stands alone, upright, leaning back slightly against the arch pedestal, screen facing the camera. In front of the pedestal lies a closed slim navy hardcover notebook, about A6 size, with a cobalt blue pen placed diagonally on top of it. Clean, orderly, calm.
```

### 6 · Pack de 30 modèles de publications
- **Pastille :** `TEMPLATE` · **Titre :** « 30 modèles / de publications »
- **Écran incrusté :** la page produit du pack, avec l'aperçu des publications.

```text
A dark-skinned hand with short clean natural nails holds the phone upright from the right side, its bottom edge resting on the arch pedestal, the phone turned slightly toward the camera. True adult scale: the phone is slightly narrower than the palm. Behind the phone, three thin square cards about 9 cm wide are fanned out like social media posts, one cobalt, one navy, one off-white, completely plain, no text, no images.
```

---

## 3. Avant de garder une variante

1. **Comparez-la à la couverture de référence**, côte à côte : même bleu de fond, même socle, même lumière. Si l'une détonne, on jette.
2. Le téléphone est **à la bonne échelle** : un peu moins large que la paume quand il y a une main, plus haut que l'objet posé à côté.
3. L'écran vert est entier, les quatre coins visibles, aucun doigt dessus.
4. Le tiers haut gauche est **vide**.
5. Aucun texte, aucun chiffre sur les objets (feuille, calendrier, cartes).

À réception, je fais le reste :
1. J'incruste la vraie page mepaye dans chaque écran, en PNG sans perte.
2. Je pose la pastille et le titre, identiques sur les sept miniatures.
3. Je remplace les couvertures à plat dans la liste des produits, le mockup « Votre boutique » et la boutique de démo.
4. Je vous montre le tout en local, sur ordinateur et à 390 px, avant toute mise en ligne.
