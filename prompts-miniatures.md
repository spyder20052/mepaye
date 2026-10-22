# Miniatures des produits de Studio Aïcha · prompts

Ces six miniatures remplacent les couvertures à plat (fonds vert et marine avec une icône) dans la liste des produits, dans le mockup « Votre boutique » et dans la boutique de démo. Chaque prompt génère **la miniature complète, texte compris, sans écran vert**, exactement comme la couverture déjà faite, « Créer et vendre des produits numériques » : on la pose telle quelle, sans retouche.

| # | Produit | Pastille | Prix | Statut |
|---|---|---|---|---|
| 0 | Ebook : créer et vendre des produits numériques | EBOOK | 3 500 XOF | **fait** (référence) |
| 1 | Modèle de facture pour freelance | TEMPLATE | 2 000 XOF | à générer (visible dans le mockup) |
| 2 | Guide : lancer sa boutique en ligne | EBOOK | 5 000 XOF | à générer (visible dans le mockup) |
| 3 | Calendrier éditorial trimestriel | TEMPLATE | 4 500 XOF | à générer (visible dans le mockup) |
| 4 | Formation courte : vendre en ligne | FORMATION | 25 000 XOF | à générer |
| 5 | Formation : tenir sa comptabilité de freelance | FORMATION | 15 000 XOF | à générer |
| 6 | Pack de 30 modèles de publications | TEMPLATE | 7 500 XOF | à générer |

**Priorité :** 1, 2 et 3, les trois visibles dans le mockup de la boutique sur l'accueil.

---

## 1. La règle de la collection (ce qui ne change jamais)

La construction de la référence, à l'identique sur les sept :

```text
┌──────────────────────────────┐
│ ( PASTILLE )      [bulle]    │  ← pastille cobalt, texte blanc en capitales
│ Titre en gras     ┌──────┐   │  ← titre marine, 2 ou 3 lignes, à gauche
│ marine            │écran │✋ │  ← un iPhone en coque cobalt, écran illustré
│ sur 3 lignes      │      │   │
│            ▟▀▀▀▀▀▀▀▀▀▙       │  ← le même socle en demi-lune cobalt
└──────────────────────────────┘
```

1. **Le texte :** en haut à gauche, une pastille cobalt `#0866FF` avec le type en capitales blanches espacées, puis le titre en gros, dans une linéale géométrique grasse, marine `#10244A`, aligné à gauche.
2. **Le décor :** fond bleu pâle `#EDF4FF`, lumière de fenêtre venant de la gauche, avec de grandes ombres douces en diagonale sur le mur et le sol blanc.
3. **Le socle :** une demi-lune cobalt mate, en bas à droite, toujours de la même taille.
4. **Le téléphone :** un iPhone en coque cobalt, posé debout sur le socle. Son écran montre une **interface illustrée simple** (cartes arrondies, vignettes, traits gris à la place du texte, boutons cobalt), comme sur la référence, avec un dessin propre au sujet.
5. **La bulle :** une bulle blanche au-dessus du téléphone, avec une icône ronde cobalt et **deux ou trois mots** en marine.
6. **Le rythme :** les miniatures paires ont une main qui tient le téléphone, comme la référence. Les impaires montrent le téléphone seul sur le socle, avec un objet posé à côté. Vue en liste, la boutique alterne sans se répéter.
7. **Les couleurs :** cobalt, marine, bleu pâle, blanc et la peau, rien d'autre.

### Le conseil qui fait la cohérence

Générez les six dans **la même conversation** (ChatGPT ou Ideogram, qui écrivent bien le texte), en joignant chaque fois la couverture déjà faite comme image de référence. Commencez par : `Use the attached cover as the exact style reference: same layout, typography, colors, lighting, pedestal and phone.`

### Le bloc de style (à coller à la fin de chaque prompt)

```text
Square 1:1 ebook and course cover thumbnail, part of a consistent series, clean premium design like a top Upwork portfolio thumbnail, photographic realism for the objects. Pale blue #EDF4FF background with soft window light from the left casting large soft diagonal window shadows on the wall and on the white floor. Top-left: a rounded pill label in cobalt blue #0866FF with white uppercase letter-spaced text, then a large title in a bold geometric sans-serif typeface, navy #10244A, left-aligned, tight line spacing. Bottom-right: a matte cobalt blue #0866FF half-moon pedestal, flat side down. A modern iPhone in a matte cobalt blue case stands upright on the pedestal, screen facing the camera, showing a clean minimal illustrated app interface: white and pale blue rounded cards, soft grey lines instead of text, small cobalt buttons. Above the phone, a small white speech-bubble notification card with a round cobalt icon and a short navy text. True real-world scale between the phone, the hand and the objects. Color world strictly cobalt blue, navy, pale blue, white and natural skin tones. Generous empty space, no logo, no other text than the one requested, no clutter.
```

### À exclure (pour toutes)

```text
misspelled text, wrong accents, extra words, gibberish text, logos, watermark, green screen, oversized phone, tiny hand, extra or fused fingers, distorted hands, waxy or plastic skin, cluttered background, more than one prop, props in other colors, warm orange cast, purple, green, oversaturated, harsh shadows, 3D cartoon style
```

---

## 2. Les six prompts

Collez chaque prompt, puis le bloc de style.
**Fichier :** `photos-a-trier/miniature-<numéro>.png`, carré, 2 048 × 2 048 px minimum.

### 1 · Modèle de facture pour freelance (sans main)

```text
Pill label text: "TEMPLATE". Title on two lines, exactly: "Facture" / "pour freelance". The phone stands alone on the pedestal. Its screen shows a minimal illustrated invoice: a cobalt header band, two grey lines, a short table of three rows with grey lines, a bold total line and a cobalt button at the bottom. In front of the pedestal, a single crisp sheet of white A5 paper lies flat on the floor, like a printed invoice with a thin cobalt band at the top and faint grey lines, no readable text. Notification bubble text, exactly: "Facture payée !"
```

### 2 · Guide : lancer sa boutique en ligne (avec main)

```text
Pill label text: "EBOOK". Title on three lines, exactly: "Lancer sa" / "boutique" / "en ligne". A dark-skinned hand with short clean natural nails holds the phone from the right side, its bottom edge resting on the pedestal, at true adult scale: the phone is slightly narrower than the palm, only the thumb and fingertips overlap the side frame. The screen shows a minimal illustrated online shop: a small store name bar with a round avatar, a large product card with an image placeholder, and a two-column grid of smaller product cards with cobalt buttons. Notification bubble text, exactly: "Boutique en ligne !"
```

### 3 · Calendrier éditorial trimestriel (sans main)

```text
Pill label text: "TEMPLATE". Title on three lines, exactly: "Calendrier" / "éditorial" / "trimestriel". The phone stands alone on the pedestal. Its screen shows a minimal illustrated monthly calendar: a header with two grey lines, a grid of rounded squares where a few squares hold small cobalt and pale blue post thumbnails, and a cobalt button at the bottom. To the left of the pedestal stands a small white desk tent calendar with a navy wire binding, its page a simple grid of empty squares with three squares filled in cobalt, no numbers. Notification bubble text, exactly: "Post planifié !"
```

### 4 · Formation courte : vendre en ligne (avec main)

```text
Pill label text: "FORMATION". Title on two lines, exactly: "Vendre" / "en ligne". A dark-skinned hand with short clean natural nails holds the phone from the right side, its bottom edge resting on the pedestal, at true adult scale: the phone is slightly narrower than the palm. The screen shows a minimal illustrated video course: a large video thumbnail of a soft blue landscape with a white play button, a thin cobalt progress bar, then a list of four lessons as rounded rows, the first one checked in cobalt. Notification bubble text, exactly: "4 modules vidéo"
```

### 5 · Formation : tenir sa comptabilité de freelance (sans main)

```text
Pill label text: "FORMATION". Title on three lines, exactly: "Tenir sa" / "comptabilité" / "de freelance". The phone stands alone on the pedestal. Its screen shows a minimal illustrated finance dashboard: a cobalt card with a large white balance shape and grey lines, a small rising line chart in cobalt, and three rounded rows of transactions with small round icons. In front of the pedestal lies a closed slim navy hardcover notebook with a cobalt pen placed diagonally on top. Notification bubble text, exactly: "Comptes à jour !"
```

### 6 · Pack de 30 modèles de publications (avec main)

```text
Pill label text: "TEMPLATE". Title on two lines, exactly: "30 modèles" / "de publications". A dark-skinned hand with short clean natural nails holds the phone from the right side, its bottom edge resting on the pedestal, at true adult scale: the phone is slightly narrower than the palm. The screen shows a minimal illustrated grid of nine square social media posts in cobalt, navy, pale blue and white, each with a simple shape or a soft photo placeholder, no text. Notification bubble text, exactly: "30 modèles prêts"
```

---

## 3. Avant de garder une variante

1. **Le texte est exact,** accents compris : « éditorial », « comptabilité », « modèles », « payée », « planifié », « vidéo », « à jour ». Au moindre mot faux, on régénère : les générateurs se trompent souvent sur les accents.
2. **Côte à côte avec la référence :** même bleu de fond, même socle, même taille de titre, même place de la pastille. Si l'une détonne, on jette.
3. Le téléphone est **à la bonne échelle** : un peu moins large que la paume quand il y a une main.
4. L'écran reste **une illustration simple** (traits gris, cartes, boutons cobalt), sans faux texte illisible.

À réception, je remplace les couvertures à plat dans la liste des produits, le mockup « Votre boutique » et la boutique de démo, puis je vous montre le tout en local, sur ordinateur et à 390 px.
