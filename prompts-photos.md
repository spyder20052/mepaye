# Photos de personnes · prompts de génération

Cinq photos du site montrent des personnes réelles. Elles seront remplacées par une même série, pensée comme **une seule campagne photo en studio**, sur le modèle des trois références : fond uni peint, vêtements de couleur assortie au fond, lumière douce de studio, et la vraie texture de la peau et des tissus.

L'illustration `famille.webp` (À propos) n'est pas concernée : c'est un dessin, pas une photo.

---

## 1. Ce qui donnait l'effet « IA », et ce que les références font mieux

| Avant | Références à suivre |
|---|---|
| Décors chargés et flous (marché, terrasse, gratte-ciel) | Fond de studio uni, peint ou en papier, sans rien d'autre |
| Peau lisse, trop parfaite | Pores visibles, petites irrégularités, reflets naturels |
| Sourires figés, tous identiques | Expressions franches et variées : regard baissé vers l'écran, rire, yeux fermés |
| Couleurs sans lien avec le site | Fond, vêtements et objets dans la même gamme de couleurs |
| T-shirts blancs génériques | Matières réelles : maille côtelée, coton épais, velours |

## 2. Le bloc de style commun

À coller **à la fin de chaque prompt**. Il garantit que les cinq images ont l'air de sortir du même shooting : même lumière, même objectif, même étalonnage.

```text
Shot as a real editorial studio campaign for an African fintech brand. Photographed on a Canon EOS R5 with an 85mm f/2 lens, eye-level, sharp focus on the eyes. Soft large key light from front-left through a big octabox, gentle fill from the right, subtle natural shadow on the backdrop. Color palette strictly limited to cobalt blue #0866FF, deep navy #10244A, pale sky blue #EDF4FF and white, plus natural skin tones. Authentic, unretouched skin with visible pores, fine texture and slight natural imperfections; real fabric texture with knit ribs, small creases and lint; natural asymmetric expression; anatomically correct hands with five fingers. Clean, airy composition with generous negative space. Subtle film grain, true-to-life colors, no HDR, no heavy retouching.
```

### Éléments à exclure

À mettre dans le champ dédié, ou à ajouter en fin de prompt avec « Avoid: ».

```text
plastic skin, airbrushed, over-smoothed, waxy, glossy CGI look, 3D render, illustration, cartoon, uncanny eyes, extra fingers, fused fingers, distorted hands, text, letters, logos, watermark, readable phone screen, busy background, bokeh city, warm orange cast, oversaturated, HDR, lens flare, perfect symmetry, stock photo pose
```

## 3. Paramètres conseillés

- **Midjourney :**
  - ajoutez `--style raw --v 7 --s 50` ;
  - joignez la référence indiquée avec `--sref` (le style) et éventuellement `--oref` (la pose).
- **ChatGPT, Gemini, Flux et les autres :**
  - joignez l'image de référence ;
  - commencez par : « Reproduis le style photographique, la lumière et la composition de l'image jointe, en appliquant cette description : ».
- **Toujours :** générez plusieurs versions et gardez celle dont **les mains et les yeux** sont irréprochables. C'est là que l'IA se trahit.

---

## 4. Les prompts, image par image

### A. La créatrice : ouverture de l'accueil et de À propos

- **Fichier à remplacer :** `assets/img/creatrice.webp`.
- **Image de référence :** la 3ᵉ, la femme au casque sur fond gris.
- **Format :** 4:5 vertical, 1600 × 2000 px au minimum.
- **Contrainte :** le personnage est détouré et posé dans l'arche, son téléphone dépassant devant. Il faut donc un **fond uni très clair**, facile à détourer.
- **Cadrage :** à mi-cuisse, tête dans le quart supérieur, avec de l'air au-dessus. Sur À propos, l'image est recadrée sur le haut (`object-position: 50% 12%`) : le visage doit rester entier dans les 40 % supérieurs.

```text
Waist-up studio portrait of a joyful young West African woman in her late twenties, long box braids falling over her shoulders, small gold hoop earrings, laughing naturally with her eyes half closed and head slightly tilted back, as if she just received good news. She holds a smartphone with a matte navy #10244A case up near her cheek in her right hand, screen facing her, the phone clearly visible and slightly in front of her body. She wears a relaxed cobalt blue #0866FF crew-neck sweatshirt in thick brushed cotton with visible texture. Plain seamless backdrop in very pale sky blue #EDF4FF, evenly lit, nothing else in the frame, clean separation between hair and background for easy cutout. Vertical 4:5, subject centered, head in the upper quarter with breathing room above, framed from mid-thigh up.
```

### B. Le coach : carte « Abidjan » de l'accueil

- **Fichier à remplacer :** `assets/img/usage-abidjan.webp`.
- **Image de référence :** la 2ᵉ, l'homme dans le fauteuil sur fond moutarde.
- **Format :** 3:2 horizontal, 1800 × 1200 px.
- **Cadrage :** l'image est affichée en 16:10, centrée un peu en hauteur (`object-position: 50% 30%`). Le visage et le téléphone doivent rester dans la bande centrale.

```text
Studio lifestyle photo of a confident West African man in his early thirties, short tapered haircut, neat short beard, sitting relaxed in a rounded white bouclé armchair, one leg crossed, talking and gesturing with an open hand toward a smartphone mounted on a small black tripod in front of him, as if recording a coaching video. Warm genuine smile, mid-sentence expression. He wears a deep navy #10244A zip bomber jacket over a white t-shirt, dark trousers, white socks and clean white sneakers. Seamless backdrop and floor in cobalt blue #0866FF with a soft gradient falloff, a single tall arch shape painted in slightly lighter blue on the wall behind him. Horizontal 3:2, subject slightly left of center, face and phone in the middle band of the frame.
```

### C. La commerçante : carte « Cotonou » de l'accueil, et chapitre « Conviction » de À propos

- **Fichier à remplacer :** `assets/img/usage-cotonou.webp`.
- **Image de référence :** la 1ʳᵉ, la femme au béret devant le mur à bandes de couleur.
- **Format :** 4:5 vertical, 1600 × 2000 px.
- **Cadrage :** sur À propos, l'image remplit une arche verticale (`object-position: 50% 15%`) ; sur l'accueil, elle est recadrée en 16:10. Le visage doit se trouver juste au-dessus du centre, le téléphone à hauteur de poitrine.

```text
Studio portrait of a West African market trader in her forties, warm round face, cobalt blue #0866FF wax-print headwrap tied high, small gold earrings, looking down at her smartphone with a soft proud smile, both hands holding the phone at chest height, the phone in a pale sky blue #EDF4FF case. She wears a fitted navy #10244A ribbed knit turtleneck with real visible knit texture. Behind her, a color-blocked painted wall in horizontal bands: deep navy #10244A at the top, a thin cobalt blue #0866FF molding stripe, a wide white band, and pale sky blue #EDF4FF at the bottom, with a subtle painted arch outline behind her head. Vertical 4:5, framed from the waist up, face just above the center, lots of clean wall above her head.
```

### D. La formatrice : carte « Dakar » de l'accueil

- **Fichier à remplacer :** `assets/img/usage-dakar.webp`.
- **Image de référence :** la 1ʳᵉ pour le mur à bandes, la 3ᵉ pour l'expression.
- **Format :** 3:2 horizontal, 1800 × 1200 px.
- **Cadrage :** recadrage 16:10 centré un peu en hauteur. Le visage doit être dans le tiers supérieur, l'ordinateur en bas du cadre.

```text
Studio lifestyle photo of a young Senegalese woman in her mid-twenties, short natural coily hair with a few flyaway strands, small silver earrings, seated at a simple white table, smiling with her eyes closed for a brief moment of satisfaction, one hand resting on the open laptop, the other lightly touching her collarbone. A smartphone with a navy #10244A case lies face down on the table next to a pale blue ceramic mug. She wears an oversized white chunky knit sweater with thin cobalt blue #0866FF stripes at the cuffs, with deep visible knit texture. Background: a seamless pale sky blue #EDF4FF wall with one large cobalt blue #0866FF arch painted behind her, the arch top curving just above her head. Horizontal 3:2, face in the upper third, laptop at the bottom edge, clean negative space on both sides.
```

### E. Les mains : section paiement de l'accueil

- **Fichier à remplacer :** `assets/img/mains.webp`.
- **Image de référence :** la 1ʳᵉ, pour les mains et le téléphone.
- **Format :** 1:1, 2000 × 2000 px.
- **Cadrage :** l'image occupe les deux tiers droits de la section, recadrée à 42 % de la hauteur ; sur mobile, c'est un bandeau de 15 rem. Le téléphone doit être au centre exact, la carte en bas à droite.
- **Carte :** le prompt demande une **carte sans texte ni logo**. Le logo mepaye s'ajoute ensuite, sinon l'IA le déforme.

```text
Close-up studio photo of two dark-skinned hands holding a smartphone horizontally with both thumbs, natural relaxed grip, short clean nails, visible knuckle texture and fine skin lines. The phone has a matte cobalt blue #0866FF case, screen facing away from the camera. The person wears a navy #10244A ribbed knit sweater, cuffs slightly pushed up. Below, on a matte white tabletop, lies a plain cobalt blue payment card with a small subtle chip and a single white arch shape printed on it, absolutely no text and no logo. Background: seamless pale sky blue #EDF4FF, soft shadow under the hands and the card. Square 1:1, phone in the exact center, card in the lower right, face not visible.
```

---

## 5. Après la génération

1. **Formats à fournir :**
   - la créatrice en **PNG**, fond intact : je m'occupe du détourage ;
   - les autres en PNG ou JPG, à la taille indiquée.
2. **Noms de fichiers :** gardez les noms ci-dessus. Je les convertis en WebP et je les remplace sur toutes les pages.
3. **Vérification avant envoi :**
   - mains : cinq doigts, ongles nets ;
   - yeux : nets et symétriques sans être parfaits ;
   - aucun texte lisible sur les écrans ;
   - aucune déformation du téléphone.
4. **Légendes de l’accueil :** les cartes Abidjan, Cotonou et Dakar affichent désormais le métier (« Coach », « Commerçante », « Formatrice ») à la place de « Sur le terrain », ce qui convient aux photos en studio.
