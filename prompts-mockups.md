# Mockups de téléphone ultra-réalistes · prompts

Ces mockups remplacent les iPhone dessinés en CSS. Le but est un rendu de photo produit Apple, comme votre référence (main, cadre en titane, studio clair), avec des mises en scène variées. L'interface doit rester lisible : chaque écran est généré en **vert chroma**, puis j'y incruste la vraie interface mepaye en haute définition.

---

## 1. Les règles qui garantissent la lisibilité

1. **Écran vert uni `#00FF00`**, mat, d'un bord à l'autre, sans reflet, sans dégradé ni interface. La Dynamic Island reste visible en noir.
2. **Angle :** l'écran fait face à la caméra à **30° près**. Au-delà, le texte de l'interface devient illisible une fois incrusté.
3. **Taille :** l'écran occupe **au moins 40 % de la hauteur** de l'image (60 % pour un téléphone seul).
4. **Les quatre coins de l'écran sont visibles.** Un pouce peut toucher un bord, jamais le centre de l'écran.
5. **Téléphone :** iPhone 17 Pro en titane naturel, sans coque, bords fins, même modèle sur toutes les images.
6. **Fond :** un studio uni, dans la couleur du panneau qui l'accueillera (indiquée pour chaque visuel), sans décor.
7. **Définition :** 3 000 px minimum sur le grand côté, en PNG.
8. **Sélection :** 6 à 8 variantes par scène. Gardez celles qui ont un écran parfaitement rectangulaire (aucune déformation) et des mains impeccables.

### Le bloc de style (à coller à la fin de chaque prompt)

```text
Ultra-realistic premium product photograph in the style of Apple marketing imagery. Modern iPhone 17 Pro in natural titanium, no case, thin uniform black bezels, Dynamic Island visible as a black pill. The entire screen is a perfectly flat, uniform, matte chroma green #00FF00 from edge to edge, no reflection, no glare, no gradient, no interface, all four rounded screen corners fully visible. Precise brushed titanium frame with realistic soft specular highlights, crisp machined edges, accurate proportions. Large soft key light from the top left, gentle rim light, soft natural contact shadows. Seamless studio backdrop, clean and minimal, generous negative space. Shot on a Hasselblad X2D, 90mm, f/8, everything on the phone tack sharp. Neutral cool color grade, clean whites, subtle grain, no HDR.
```

### À exclure

```text
text, logos, watermark, user interface on screen, screen reflections, glare on screen, notch, phone case, warped or curved screen, fingers covering the screen center, extra or fused fingers, distorted hands, busy background, props, colored lights, oversaturated, CGI plastic look, low resolution
```

---

## 2. Les mockups, section par section

| Code | Section | Mise en scène | Fond | Écran incrusté |
|---|---|---|---|---|
| **M1** | Hero | le téléphone debout, comme une sculpture | blanc | page produit de Studio Aïcha |
| **M2** | Votre boutique | deux téléphones flottants, l'un devant l'autre | bleu pâle `#EFF6FF` | accueil + produits de la boutique |
| **M3** | Plusieurs marques | trois téléphones en éventail | gris clair `#F4F4F5` | trois boutiques différentes |
| **M4** | Décrivez votre idée | la main qui tend le téléphone, contre-plongée | jaune pâle `#FEF3C7` | génération de l'ebook par l'IA |
| **M5** | Le paiement | le gros plan sur la notification | bleu pâle `#EFF6FF` | notification « Nouvelle vente » |
| **M6** | Réserve (pages annexes) | le téléphone posé à plat, vu en plongée | gris clair `#F4F4F5` | au choix |

### M1 · Le téléphone debout (hero)
**Fichier :** `mockup-hero.png` · **Format :** 4:5, 3 000 × 3 750 px.
- **Usage :** il est détouré puis placé au centre de l'arche, entre l'acheteur et la créatrice. Il remplace le téléphone géant actuel.

```text
A single smartphone standing upright on its bottom edge on a seamless pure white studio floor, perfectly vertical, rotated about 12 degrees toward the right so the left titanium side frame and side buttons are slightly visible, screen facing the camera. Camera at the height of the phone's middle, very slight low angle, so the phone feels monumental like a sculpture. A soft natural contact shadow and a faint reflection on the glossy white floor. The phone fills 85 percent of the frame height. Vertical 4:5, nothing else in the frame.
```

### M2 · Les deux téléphones flottants (Votre boutique)
**Fichier :** `mockup-boutique.png` · **Format :** 16:9, 3 840 × 2 160 px.

```text
Two identical smartphones floating in mid-air on a seamless pale blue #EFF6FF studio backdrop, both screens facing the camera. The front phone stands slightly right of center, tilted 6 degrees clockwise. The back phone stands left of center, a little higher and a little smaller, tilted 6 degrees counter-clockwise, its right edge partly hidden behind the front phone but its whole screen visible. Soft separate shadows fall on the backdrop behind each phone, suggesting depth. Each phone fills about 75 percent of the frame height. Horizontal 16:9, wide empty space on the far left and far right.
```

### M3 · Les trois téléphones en éventail (Plusieurs marques)
**Fichier :** `mockup-marques.png` · **Format :** 16:9, 3 840 × 2 160 px.

```text
Three identical smartphones arranged like a fanned hand of cards on a seamless very light grey #F4F4F5 studio backdrop, all screens facing the camera. The center phone stands upright in front. The left and right phones sit slightly behind it, each rotated outward by about 14 degrees and offset upward a little, their screens mostly visible beside the center phone. Soft layered shadows between the phones give a clear sense of depth. The group fills 80 percent of the frame height. Horizontal 16:9, centered composition, generous empty space on both sides.
```

### M4 · La main qui tend le téléphone (Décrivez votre idée)
**Fichier :** `mockup-creation.png` · **Format :** 16:9, 3 840 × 2 160 px.
- **Référence :** votre image de la main, dont on reprend l'esprit, avec un angle moins fort pour garder le texte lisible.

```text
Low-angle hero shot of a dark-skinned hand holding a smartphone from behind and below, fingertips lightly gripping the side frames, the phone tilted back about 25 degrees toward the viewer so the screen faces the camera and the bottom titanium edge and speaker grille are visible in the foreground. The hand is softly lit and slightly out of focus, the phone and its screen are tack sharp. Seamless pale butter yellow #FEF3C7 studio backdrop with a soft gradient toward white at the top. The phone fills 70 percent of the frame height, placed right of center. Horizontal 16:9, empty space on the left.
```

### M5 · Le gros plan sur la notification (Le paiement)
**Fichier :** `mockup-notification.png` · **Format :** 16:9, 3 840 × 2 160 px.
- **Usage :** j'y incruste la notification « Nouvelle vente · 3 500 XOF avec Wave » en haut de l'écran, bien lisible, au-dessus de la grille des moyens de paiement.

```text
Macro close-up of the top third of a smartphone seen from slightly above, tilted back about 20 degrees, the Dynamic Island and the top of the screen filling most of the frame, the titanium frame edge catching a fine highlight. Only the upper part of the phone is in the frame, cropped at the bottom by the image edge. Seamless pale blue #EFF6FF backdrop. Very shallow depth of field at the lower crop, top of the screen tack sharp. Horizontal 16:9, phone centered.
```

### M6 · Le téléphone posé à plat (réserve pour les pages annexes)
**Fichier :** `mockup-plat.png` · **Format :** 4:3, 4 000 × 3 000 px.

```text
A smartphone lying flat on a seamless very light grey #F4F4F5 surface, photographed from above at a 35 degree angle, rotated about 20 degrees so it sits diagonally in the frame, screen facing up toward the camera. A long soft shadow falls to the lower right. The phone fills 65 percent of the frame width. Horizontal 4:3, generous empty space around it.
```

---

## 3. Me les envoyer

1. Déposez les images retenues dans `photos-a-trier/`, sous les noms indiqués (`mockup-hero.png`, `mockup-boutique.png`…).
2. Pour chacune :
   - je recapture l'écran voulu en PNG sans perte, avec un contenu plus vendeur dans le même contenant ;
   - je l'incruste en perspective à la résolution Retina ;
   - je détoure le hero.
3. Je vous montre chaque section sur ordinateur et à 390 px, en local. Rien ne part en ligne sans votre demande.

**Priorité conseillée :** M1 (le hero, vu en premier), puis M2 et M4, qui transforment les deux sections les plus visibles après lui.
