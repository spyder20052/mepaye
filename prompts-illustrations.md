# Illustrations de la landing · prompts à générer

Un seul shooting fictif, dans la suite de la campagne « La porte » (`campagne-photo.md`) : même lumière, même palette, mêmes coques bleues. Chaque image montre une vraie personne avec l'application mepaye en main. Les écrans seront remplis par mes soins avec les vraies interfaces : le contenant reste celui des captures, seul le contenu change.

---

## 1. Les règles pour que l'intégration soit parfaite

1. **Écran vert :** quand l'écran est tourné vers la caméra, il doit être d'un **vert chroma uni `#00FF00`**, sans reflet, sans dégradé et sans interface, d'un bord à l'autre.
   - Le vert se détoure mieux que le blanc. Le blanc se confond avec les reflets, les t-shirts blancs et les ongles clairs.
   - Les doigts peuvent mordre un peu sur le bord de l'écran : le vert permet de les garder devant.
2. **Angle de l'écran :** de face ou incliné de 25° au plus. Au-delà, l'interface devient illisible une fois incrustée.
3. **Téléphone :** un iPhone récent, avec Dynamic Island (une pilule noire, pas d'encoche), coque mate **bleu cobalt `#0866FF`**. Toujours le même modèle d'une image à l'autre.
4. **Fond :** un studio uni, sans décor, dans la couleur du panneau qui accueillera l'image (indiquée pour chaque visuel). Il faut les mêmes teintes partout pour que la photo se fonde dans le panneau arrondi.
5. **Format :** 3 000 px minimum sur le grand côté. Pour les bandeaux en 16:9, la personne est au centre, avec beaucoup d'espace vide à gauche et à droite : j'y pose les pastilles (« Mobile Money », « Dès validation »…).
6. **Sélection :** 6 à 8 variantes par scène. Gardez celles qui ont des **mains et des yeux parfaits**, et des bijoux identiques des deux côtés.
7. **Envoi :** déposez les images dans `photos-a-trier/`, sous les noms indiqués.

### Le bloc de style (à coller à la fin de chaque prompt)

```text
Premium Apple-style brand campaign photograph for a mobile payment app. Shot on a Hasselblad X2D with an 80mm lens at f/2.8, soft large key light from the left at 45 degrees, gentle rim light, tender natural shadows. Color world limited to cobalt blue #0866FF, sky blue #BFD6FF, pale blue #EFF6FF, off-white, navy #10244A and natural skin tones. Clean, airy, minimal composition with generous negative space. Authentic skin with visible pores and fine texture, real knit and cotton texture, natural asymmetric expression, anatomically correct hands with five fingers. Modern iPhone with a Dynamic Island pill cutout, no notch, matte cobalt blue case. Cool soft color grade, clean whites, subtle film grain, no HDR.
```

### À exclure

```text
plastic skin, airbrushed, CGI, 3D render, illustration, extra or fused fingers, distorted hands, text, letters, logos, watermark, user interface on screen, screen reflections, notch, busy background, office, street, clouds, warm orange cast, oversaturated, HDR, stock photo pose, thumbs up, fist pump, perfect symmetry
```

---

## 2. Le hero : « Créez. Vendez. Encaissez. » en une seule image

### L'idée

Sous le titre centré, une grande **arche bleu pâle**, entière, comme celle du logo, se lève depuis le bas de l'écran. Au centre de l'arche se dresse un **téléphone géant**, plus grand qu'un humain, qui affiche la vraie boutique d'une créatrice. Je le construis en CSS : il reste net à toute taille, et l'écran est la vraie interface.

De part et d'autre, deux personnes détourées racontent la phrase du titre, de gauche à droite, dans le sens de l'argent :

```text
                 Créez. Vendez. Encaissez.
             Commencer gratuitement →  Se connecter

                  ╭──────────────────────╮
                ╭─┤   ┌──────────────┐   ├─╮
               │      │  ▬ island    │      │   ◯ Paiement reçu · 14 900 XOF · Wave
               │      │  Boutique    │      │       (bulle qui flotte au-dessus d'elle)
               │      │  Studio Aïcha│      │
      L'ACHETEUR      │  [Acheter]   │      LA CRÉATRICE
      assis au sol,   │              │      debout, elle rit en lisant
      il paie         │   téléphone  │      sa notification
               │      │    géant     │      │
  ─────────────┴──────┴──────────────┴──────┴──────────  (ombres de contact au sol)
```

- **Le mouvement, mesuré :** au chargement, le téléphone géant monte doucement. Puis, toutes les 3 secondes, une notification apparaît au-dessus de la créatrice et alterne entre Wave, Orange Money et MTN MoMo (logo bleu sur fond blanc, comme dans l'app). Avec le mouvement réduit, l'image reste fixe, sur la première notification.
- **Ce qui la distingue de Taptap Send :** pas de bande de couleur ni de pose accroupie. L'arche de la marque, deux personnes et une histoire qui se lit d'un coup d'œil : quelqu'un paie, quelqu'un encaisse, entre les deux il y a la boutique mepaye.
- **Sur mobile :** le téléphone géant et la créatrice seule, posée devant le bord droit du téléphone, plus grande, pour garder l'effet « waouh » sur 390 px.

### H1 · La créatrice, debout
**Fichier :** `hero-creatrice.png` · **Format :** 4:5 vertical, 3 000 × 3 750 px · **Fond :** blanc uni, pour le détourage.
**Joindre :** `photos-a-trier/creatrice.webp` comme référence de personnage (c'est la même femme).

```text
Full-body studio photograph of the same young West African woman as the reference image: long knotless box braids, small gold hoops, heavyweight off-white cotton t-shirt, light blue straight-leg jeans, clean white leather sneakers. She stands in a relaxed three-quarter pose turned slightly to the left of the frame, holding her smartphone at chest height in her right hand, screen facing her, and she bursts into a genuine laugh as she reads it, her free left hand lifted lightly toward her collarbone in delighted surprise. Camera at waist height, very slight low angle. Plain seamless pure white backdrop and white floor, evenly lit, a soft natural contact shadow under her feet, nothing else in the frame, crisp separation between braids and background for a clean cutout. Vertical 4:5, whole body visible from head to shoes with space above the head.
```

### H2 · L'acheteur, assis au sol
**Fichier :** `hero-acheteur.png` · **Format :** 4:5 vertical, 3 000 × 3 750 px · **Fond :** blanc uni.

```text
Full-body studio photograph of a relaxed West African man in his late twenties, short tapered fade, neat short beard, wearing a navy #10244A heavy knit crewneck sweater, off-white chino trousers and clean white sneakers. He sits on the floor turned three-quarter toward the right of the frame, one knee raised, leaning back on his left hand, holding his smartphone in his right hand at face level, screen facing him, thumb about to tap, with a calm satisfied smile as if he is paying for something he really wanted. Camera at waist height, the same lens and lighting as a matching campaign portrait, soft key light from the left. Plain seamless pure white backdrop and white floor, evenly lit, soft natural contact shadow under him, nothing else in the frame. Vertical 4:5, whole body visible with space around him.
```

> Les deux images doivent avoir **la même lumière (de gauche) et la même hauteur de caméra**. Générez la créatrice d'abord, puis joignez-la comme référence de style pour l'acheteur.

---

## 3. Les visuels des sections, dans l'ordre de la page

Chaque photo occupe tout le panneau arrondi de sa section, sous le titre, à la place de la capture actuelle. Les pastilles de la section flottent dans l'espace vide autour de la personne.

| Section | Visuel | Écran incrusté (contenu enjolivé) |
|---|---|---|
| Votre boutique | aucun, on garde les deux téléphones | |
| Le paiement, sous toutes ses formes | `mains.webp`, **déjà là** | le choix du moyen de paiement, Wave sélectionné |
| Votre argent, sur votre Mobile Money | **R1**, elle montre son solde | wallet : 920 000 XOF, « Retirer mes gains » |
| Décrivez votre idée. Mepaye rédige. | **C1**, l'ebook qui s'écrit | génération IA : plan, chapitres, « Prêt à publier » |
| Une boutique à votre image | **V1**, par-dessus l'épaule | page produit « Le programme Wellness 30 jours », 14 900 XOF |
| Vos clients deviennent vos vendeurs | **A1**, elle montre à son amie | affiliation : lien `mepaye.shop/r/aicha`, 47 500 XOF de commissions |
| Chaque décision, appuyée par vos chiffres | **N1**, le doigt sur la courbe | tableau de bord : 847 200 XOF ce mois-ci, courbe qui monte |

Les autres sections (marques, produits, avis, pourquoi Mepaye) gardent leurs captures ou leurs cartes. Les avis restent avec leurs initiales : mettre un visage généré à côté d'un vrai prénom inventerait une personne.

### R1 · Elle montre son solde
**Fichier :** `revenus-solde.png` · **Format :** 16:9, 3 840 × 2 160 px · **Fond :** bleu très pâle `#EFF6FF`.

```text
Waist-up studio portrait of a joyful young West African woman in her mid-twenties with short natural coily hair, small gold studs, wearing a soft sky blue #BFD6FF chunky knit sweater. She holds her smartphone out toward the camera at arm's length in her right hand, screen facing the camera, tilted no more than 15 degrees, and points at the screen with her left index finger, beaming with a proud open smile, looking straight into the lens as if saying "look what I earned". The phone screen is a perfectly flat uniform chroma green #00FF00, edge to edge, no reflection, no interface. Plain seamless pale blue #EFF6FF backdrop. Horizontal 16:9, she is centered, phone sharp in the foreground, wide empty space on both sides of her.
```

### C1 · L'ebook qui s'écrit
**Fichier :** `creation-ia.png` · **Format :** 16:9, 3 840 × 2 160 px · **Fond :** jaune très pâle `#FEF3C7` (le panneau de la section est jaune).

```text
Studio portrait of a young West African man in his early twenties with short twists, thin gold-rimmed glasses, wearing an off-white heavy knit sweater. He sits cross-legged on a low white bench and holds his smartphone in both hands at chest height, screen turned three-quarter toward the camera, tilted no more than 25 degrees, looking down at it with a delighted, slightly amazed smile, as if his ebook just wrote itself. The phone screen is a perfectly flat uniform chroma green #00FF00, edge to edge, no reflection, no interface. Plain seamless very pale butter yellow #FEF3C7 backdrop and floor. Horizontal 16:9, he is centered, wide empty space on both sides.
```

### V1 · Par-dessus l'épaule
**Fichier :** `vitrine-epaule.png` · **Format :** 16:9, 3 840 × 2 160 px · **Fond :** bleu très pâle `#EFF6FF`.

```text
Over-the-shoulder studio shot of a West African woman in her thirties with a pale sky blue headwrap tied high, small gold earrings, cream ribbed knit turtleneck, holding her smartphone in her right hand in front of her, browsing an online shop. The camera looks over her left shoulder: her shoulder, headwrap and cheek are softly out of focus in the foreground on the left third, the phone is sharp in the center, held upright and facing the camera almost straight on, her thumb resting on the lower edge. The phone screen is a perfectly flat uniform chroma green #00FF00, edge to edge, no reflection, no interface. Plain seamless pale blue #EFF6FF backdrop. Horizontal 16:9, empty space on the right.
```

### A1 · Elle montre à son amie
**Fichier :** `affiliation-amies.png` · **Format :** 16:9, 3 840 × 2 160 px · **Fond :** bleu très pâle `#EFF6FF`.
**Joindre :** `photos-a-trier/communaute.webp` comme référence de style.

```text
Studio photograph of two West African friends in their twenties, side by side. The woman on the left, long braids, pale blue chunky knit sweater, turns her smartphone toward the camera at chest height, screen facing the camera, tilted no more than 20 degrees, and smiles proudly. Her friend on the right, short afro, cream ribbed cardigan, leans in close with her head near her shoulder, looking at the screen with an impressed laugh. The phone screen is a perfectly flat uniform chroma green #00FF00, edge to edge, no reflection, no interface. Plain seamless pale blue #EFF6FF backdrop. Horizontal 16:9, both friends in the center, wide empty space on both sides.
```

### N1 · Le doigt sur la courbe
**Fichier :** `analytics-main.png` · **Format :** 16:9, 3 840 × 2 160 px · **Fond :** gris très clair `#F4F4F5` (le panneau de la section est gris).

```text
Close-up studio photograph of a dark-skinned man's hands holding a smartphone upright, left hand gripping the phone from below, right index finger lightly touching the upper half of the screen as if tracing a growth chart, the cuff of a navy #10244A heavy knit sweater visible at both wrists, a slim steel watch on the left wrist. The phone faces the camera straight on, tilted no more than 10 degrees. The phone screen is a perfectly flat uniform chroma green #00FF00, edge to edge, no reflection, no interface, the fingertip crisp in front of it. Plain seamless very light grey #F4F4F5 backdrop, soft shadow of the hands. Horizontal 16:9, the phone slightly right of center, empty space on the left.
```

---

## 4. Ce que je fais à réception

1. Je détoure la créatrice et l'acheteur du hero, et je monte la scène avec l'arche et le téléphone géant.
2. Je prépare les écrans : les vraies interfaces de l'app, avec un contenu plus vendeur (soldes, ventes, produits de Studio Aïcha). Le contenant reste identique aux captures.
3. J'incruste chaque écran en perspective dans le vert, en gardant les doigts devant.
4. J'harmonise l'étalonnage, je convertis en WebP et je vous montre chaque section sur ordinateur et à 390 px, en local. Rien ne part en ligne sans votre demande.
