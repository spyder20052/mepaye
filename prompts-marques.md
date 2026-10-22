# « Une identité. Plusieurs marques. » · la nouvelle section

## L'idée : trois créateurs, trois boutiques, une seule arche

Les trois téléphones de face sont remplacés par **trois portraits dans trois arches**, côte à côte. Chaque arche reprend la forme du logo. Dans chacune, une personne heureuse tend son téléphone vers nous, et l'écran montre **sa propre boutique** mepaye.

Sous chaque arche, une ligne :
- le nom de la boutique, Studio Aïcha, Wellness Pro ou Digital Habit ;
- son adresse en gris, `studio-aicha.mepaye.shop` par exemple.

```text
   ╭───────╮        ╭───────╮        ╭───────╮
  │  ☺ 📱  │      │  ☺ 📱  │      │  ☺ 📱  │      ← trois arches entières, même taille
  │ Studio │      │Wellness│      │ Digital│        chaque écran = sa boutique
  │ Aïcha  │      │  Pro   │      │ Habit  │
  └───────┘        └───────┘        └───────┘
  Studio Aïcha     Wellness Pro     Digital Habit
  studio-aicha…    wellness…        habit…
```

**Pourquoi c'est plus clair :** on comprend sans lire que trois personnes différentes ont chacune leur marque, sous la même maison mepaye. C'est exactement « Une identité. Plusieurs marques. ».

- **Couleurs :** chaque boutique a sa couleur de marque sur l'écran : bleu pour Studio Aïcha, vert sauge pour Wellness Pro, violet pour Digital Habit. C'est le seul endroit coloré, ce qui montre « chacune son style ».
- **Mobile :** les trois arches défilent à l'horizontale, au doigt, la suivante dépassant un peu du bord.
- **Écrans :** je recompose les trois vitrines à partir de la vraie page boutique de l'app, avec leurs noms, couleurs et produits. Le contenant reste celui de l'app, seul le contenu change.

---

## Les règles communes (pour que les trois images forment une série)

1. **Même cadrage :** à mi-cuisse, la personne centrée, la tête dans le tiers supérieur, de l'air au-dessus de la tête (l'arche arrondit le haut).
2. **Même fond :** studio uni bleu très pâle `#EFF6FF`, même lumière douce venant de la gauche.
3. **Le téléphone :** iPhone 17 Pro en titane naturel, sans coque, tenu d'une main à hauteur de poitrine, **écran tourné vers la caméra**, de face à 15° près. L'écran est d'un **vert uni `#00FF00`**, d'un bord à l'autre. Les quatre coins sont visibles, aucun doigt sur l'écran, seulement sur les bords.
4. **L'expression :** une vraie fierté joyeuse, comme quelqu'un qui montre sa boutique à un ami. Pas de pouce levé.
5. **Les mains :** belles, soignées, cinq doigts bien dessinés. C'est le premier signe d'une image générée : gardez la meilleure variante.
6. **Format :** 4:5 vertical, 3 000 × 3 750 px. Fichiers `photos-a-trier/marque-1.png`, `marque-2.png` et `marque-3.png`.

### Le bloc de style (à coller à la fin de chaque prompt)

```text
Premium Apple-style brand campaign portrait. Shot on a Hasselblad X2D, 80mm, f/4, large soft key light from the left, gentle rim light, tender shadows. Seamless pale blue #EFF6FF studio backdrop, nothing else in the frame. She or he holds a modern iPhone 17 Pro in natural titanium, no case, in one hand at chest height, screen facing the camera straight on, the entire screen a flat uniform matte chroma green #00FF00 edge to edge, no reflection, all four rounded corners visible, fingers only on the side frames, Dynamic Island visible. Authentic skin texture, natural joyful pride, beautifully groomed hands with five fingers. Vertical 4:5, framed from mid-thigh up, head in the upper third, generous space above the head. Cool soft color grade, clean whites, subtle grain.
```

### À exclure

```text
thumbs up, fingers on the screen, phone case, screen reflection, user interface on screen, text, logos, watermark, extra or fused fingers, distorted hands, busy background, props, harsh shadows, oversaturated, plastic skin, CGI
```

---

## Les trois portraits

### 1 · Studio Aïcha (la créatrice de la campagne)
**Joindre :** `photos-a-trier/creatrice.webp` comme référence de personnage.

```text
The same young West African woman as the reference image, long knotless box braids over one shoulder, small gold hoops, heavyweight off-white cotton t-shirt, light blue jeans. She holds the phone toward the camera with her right hand and rests her left hand lightly on her chest, laughing with proud joy, looking straight into the lens.
```

### 2 · Wellness Pro (le coach bien-être)

```text
A fit West African man in his early thirties, short tapered fade, neat beard, wearing a soft sage green knit polo over cream trousers. He holds the phone toward the camera with his left hand, his right hand open in a relaxed presenting gesture beside it, with a warm confident smile, looking into the lens.
```

### 3 · Digital Habit (la formatrice digitale)

```text
A young West African woman in her mid-twenties with a short natural afro and thin gold glasses, wearing an oversized lavender knit sweater. She holds the phone toward the camera with both hands at chest height, thumbs on the side frames, beaming with pride, slightly tilting her head, looking into the lens.
```

---

## À réception

1. Je détoure chaque portrait et je le pose dans son arche, avec le même sol et la même ombre.
2. Je recompose les trois vitrines et je les incruste en haute définition, avec la vraie barre d'état iOS.
3. Je vous montre la section en local, sur ordinateur et à 390 px, avant toute mise en ligne.
