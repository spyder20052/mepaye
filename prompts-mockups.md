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
| **M4** | Décrivez votre idée | la main qui tend le téléphone, contre-plongée | bleu pâle `#EFF6FF` | génération de l'ebook par l'IA |
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
**Fichier :** `mockup-creation.png` · **Format :** 16:9, 3 840 × 2 160 px · **Fond :** bleu pâle `#EFF6FF`.

**Ce qui n'allait pas dans les versions précédentes :**
- le téléphone fait presque deux fois la taille de la main ;
- la caméra est plate et lointaine, l'image ressemble à un rendu 3D ;
- la main est lisse et cireuse, avec des doigts posés au hasard.

**La direction :** une vraie photo publicitaire, prise par un photographe. La caméra est placée en trois quarts, légèrement sous le téléphone, avec une légère inclinaison qui donne du mouvement. Le téléphone est net, la main garde sa texture et le poignet se perd doucement dans le flou. Tout est à l'échelle réelle.

**Cadrage :** sur téléphone, le site recadre l'image en carré, vers la droite. La main et le téléphone restent dans la moitié droite, avec de l'air jusqu'au bord droit.

```text
SUBJECT: A professional advertising photograph of an adult man's right hand holding a modern iPhone 17 Pro in natural titanium, no case, presenting its screen toward the camera, like a product hero shot for a tech brand.

GRIP: Natural, relaxed one-hand grip. The bottom third of the phone rests in the palm. The thumb lies along the left side frame, bent at the joint, its tip reaching about 40 percent of the phone's height. The index, middle and ring fingers wrap around the right side frame, only their tips and first joints visible beyond the edge, slightly spread, touching the frame with gentle pressure; the little finger supports the bottom right corner. No finger touches the screen.

TRUE SCALE, critical: the phone is 150 mm tall, 72 mm wide, 8.75 mm thick. The hand is an average adult male hand, 190 mm long with a palm 88 mm wide. The phone is slightly narrower than the palm, the top half of the phone rises above the fingers, and the hand clearly wraps around it. The hand and the phone are at the same distance from the camera, no forced perspective.

CAMERA: Three-quarter view. The camera sits slightly below the phone and about 30 degrees to its left, looking slightly up, shot with a 100mm lens from about 1.3 meters, so there is no wide-angle distortion. The phone is turned so its left titanium side frame and the side buttons are visible, the screen still facing the camera within 25 degrees. A subtle 8 degree dutch tilt with the top of the phone leaning toward the left gives a sense of movement, as if the camera is slowly orbiting around the phone. Focus on the screen and the front of the phone, aperture f/5.6: the fingertips are sharp, the wrist and forearm fall softly out of focus toward the bottom edge.

PHONE ACCURACY: Accurate iPhone 17 Pro proportions, thin uniform black bezels, rounded screen corners matching the frame, Dynamic Island as a small black pill at the top, brushed titanium frame with crisp machined edges and soft specular highlights, correct side buttons, camera plateau not visible. The entire screen is a perfectly flat, uniform, matte chroma green #00FF00 from edge to edge, no reflection, no interface, all four rounded corners fully visible.

HAND REALISM: Dark brown skin with real texture: visible pores, fine creases on the knuckles and the palm, subtle veins on the back of the hand, natural variation of tone between palm and back, short clean natural nails with real cuticles, no lotion shine. Anatomically correct, exactly five fingers, natural knuckle proportions, relaxed tendons.

LIGHT AND SET: Large soft key light from the top left, a white bounce card on the right to open the shadows in the palm, a thin rim light outlining the titanium frame. Seamless pale blue #EFF6FF studio backdrop with a soft gradient toward white at the top, a faint soft shadow behind the hand.

FRAMING: Horizontal 16:9. The hand and phone are placed right of center and fill about 80 percent of the frame height, with clear empty space on the left and a margin on the right; only the forearm is cut by the bottom edge.

STYLE: Shot on a Phase One IQ4 with a 100mm macro lens, natural color, true-to-life skin tones, fine film grain, editorial product photography, photorealistic, not a 3D render.
```

**À exclure :**

```text
oversized phone, giant phone, tiny hand, small hand, child hand, long elongated fingers, extra or missing fingers, fused fingers, claw grip, fingers floating off the frame, finger on the screen, waxy skin, plastic skin, airbrushed skin, glossy skin, wide-angle lens, fisheye, forced perspective, flat frontal view, phone case, curved or warped screen, interface on screen, screen reflection, CGI, 3D render, cartoon, oversaturated, busy background, props, text, logo, watermark
```

**Selon l'outil :**
- **Midjourney :** ajoutez `--ar 16:9 --style raw --stylize 50` à la fin. `raw` limite l'effet « image IA ».
- **ChatGPT ou Gemini :** collez le prompt tel quel, puis demandez une retouche ciblée si un détail cloche (« make the hand 15 % larger relative to the phone »).

**L'astuce qui change tout :** photographiez avec votre propre téléphone une vraie main qui tient un iPhone dans cette pose, de trois quarts et légèrement par en dessous. Joignez cette photo comme **image de référence de pose** avec la mention `Match the exact hand pose, grip and phone-to-hand scale of the reference photo.` Les proportions viennent alors du réel, pas de l'outil.

**Contrôle avant de garder une variante :**
1. **Échelle :** le téléphone est un peu moins large que la paume, et le pouce couvre environ 40 % de sa hauteur.
2. **Prise :** les doigts touchent le cadre et le contournent ; on ne voit que le bout de trois doigts à droite.
3. **Téléphone :** bords fins et réguliers, Dynamic Island petite et centrée, écran vert entier avec ses quatre coins visibles.
4. **Peau :** du grain, des plis et des pores ; si elle paraît lisse, on jette.
5. **Netteté :** l'écran et le bout des doigts sont nets, le poignet est flou.

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
