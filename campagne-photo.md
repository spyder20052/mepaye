# Campagne photo mepaye · « La porte »

Un seul shooting, pensé comme une campagne Apple, décliné sur tout le site. Ce document remplace `prompts-photos.md` et `guide-photos.md`.

---

## 1. L'idée

**La porte mepaye.** L'arche du logo devient un vrai décor : une niche en arche, bâtie en studio et peinte dans le bleu de la marque. Chaque créateur est photographié devant, dans ou à travers cette arche, avec son téléphone, au moment où il reçoit une vente.

Deux décors seulement, qui se répondent :

| Décor | Ce que c'est | Références qui l'inspirent |
|---|---|---|
| **A. L'atelier bleu** | Un studio dont les murs, le sol et une grande niche en arche sont peints d'un seul bleu doux. La lumière est franche et douce, comme une journée claire. | le garçon assis dans le demi-cercle bleu, le portrait sur fond gris |
| **B. Le ciel** | Contre-plongée, la personne cadrée sur un ciel bleu pur, sans nuage ni bâtiment. Le ciel prolonge le bleu de la marque. | la femme au téléphone vert sur ciel, le duo en contre-plongée |

Il n'y a pas de bureau, pas de rue et pas de décor réel : tout se passe dans le bleu de la marque. C'est ce qui donne l'unité de campagne.

## 2. Les règles du shooting (communes à toutes les images)

- **Palette du décor :**

  | Teinte | Code |
  |---|---|
  | Bleu de la marque | `#0866FF` |
  | Bleu ciel doux | `#BFD6FF` |
  | Bleu très pâle | `#EDF4FF` |
  | Blanc cassé | `#F7F9FD` |

  Aucune autre couleur de fond.
- **Garde-robe :** des mailles épaisses et des cotons mats, en blanc, crème, bleu marine `#10244A` ou bleu ciel. Une seule pièce de couleur forte par personne, toujours dans les bleus. Pas de logo, pas de motif chargé, pas de noir intégral.
- **Téléphones :** coques mates unies, en bleu, blanc ou marine, toutes du même modèle. L'écran est tourné vers la personne ou vide : on y incruste ensuite le vrai écran mepaye.
- **Lumière :**
  - une grande source douce venant de la gauche, à 45° ;
  - un léger contre-jour qui détache les cheveux ;
  - des ombres présentes mais tendres.
- **Optique :** 50 mm ou 85 mm à f/2,8, à hauteur de regard pour l'atelier, contre-plongée franche pour le ciel. Peau et tissus nets, fond légèrement doux.
- **Casting :** des créateurs d'Afrique de l'Ouest francophone de 22 à 50 ans, aux styles et aux morphologies variés. Leur attitude est vraie : rire, regard vers l'écran, fierté tranquille. Pas de pose de banque d'images, pas de pouce levé.
- **Retouche :**
  - on garde le grain de peau, les pores et les petites imperfections ;
  - l'étalonnage est froid et doux, avec des blancs propres et des noirs jamais bouchés ;
  - une légère texture de pellicule.
- **Taille de livraison :** 3 000 px minimum sur le grand côté, en PNG ou JPG qualité maximale.

## 3. Le bloc de style (à coller à la fin de chaque prompt)

```text
Shot as a premium Apple-style brand campaign for "mepaye", a mobile payment platform for African creators. Photographed on a Hasselblad X2D with an 80mm lens at f/2.8, soft large key light from the left at 45 degrees, gentle rim light, tender natural shadows. Color world strictly limited to cobalt blue #0866FF, soft sky blue #BFD6FF, pale blue #EDF4FF, off-white, navy #10244A and natural skin tones. Clean, airy, minimal composition with generous negative space. Authentic unretouched skin with visible pores and fine texture, real fabric texture with knit ribs and soft creases, natural asymmetric expression, anatomically correct hands with five fingers. Cool soft color grade, clean whites, subtle film grain, no HDR.
```

### Ce qu'il faut exclure

```text
plastic skin, airbrushed, waxy, CGI, 3D render, illustration, uncanny eyes, extra or fused fingers, distorted hands, text, letters, logos, watermark, readable phone screen, busy background, office, street, city, clouds, warm orange cast, oversaturated, HDR, lens flare, stock photo pose, thumbs up, perfect symmetry
```

## 4. Bien générer

- **Midjourney (le plus proche du rendu Apple) :**
  - ajoutez `--style raw --v 7 --s 60` ;
  - joignez une référence de style commune à toutes les images avec `--sref`, par exemple la photo du garçon dans le demi-cercle bleu ;
  - pour garder **la même créatrice** d'une image à l'autre, joignez son premier portrait réussi avec `--oref` (référence de personnage).
- **ChatGPT, Gemini ou Flux :**
  - joignez la référence et commencez par : « Reproduis la lumière, la palette et la qualité photo de l'image jointe, avec la scène suivante : » ;
  - générez en format portrait 4:5, sauf indication contraire.
- **Toujours :** générez 6 à 8 variantes par scène et gardez celle aux **mains et yeux parfaits**. C'est le premier signe d'une image générée.

---

## 5. Les scènes, emplacement par emplacement

### 1. La créatrice : ouverture de l'accueil, et À propos
**Fichier :** `creatrice.webp` · **Décor :** atelier, fond uni, pour le détourage · **Format :** 4:5, 3 000 × 3 750 px.

- **Usage :** elle est détourée puis posée dans l'arche en céramique, son téléphone dépassant devant l'arche. Il faut donc un **fond uni très clair**, sans arche derrière elle.
- **Continuité :** on garde l'esprit de l'image actuelle que vous aimez (tresses, haut blanc, téléphone bleu, grand rire, regard vers le côté), avec un vrai réalisme de shooting.
- **Cadrage :** à mi-cuisse, tête dans le quart supérieur, téléphone tenu à gauche de l'image, à hauteur d'épaule.

```text
Waist-up studio portrait of a radiant West African woman in her late twenties with long knotless box braids falling over one shoulder, small gold hoops, laughing with genuine joy and looking off to the right as if she just received a payment notification. She raises a smartphone with a matte cobalt blue case in her right hand at shoulder height on the left side of the frame, screen facing her. She wears a heavyweight off-white cotton t-shirt with a visible weave. Plain seamless backdrop in very pale blue #EDF4FF, evenly lit, nothing else in the frame, crisp separation between braids and background for easy cutout. Vertical 4:5, head in the upper quarter, framed from mid-thigh up.
```

### 2. Le coach : carte « Abidjan » des avis
**Fichier :** `usage-abidjan.webp` · **Décor :** atelier, assis dans la niche en arche · **Format :** 4:5, 3 000 × 3 750 px.

- **Usage :** recadré en bandeau 16:10, centré un peu en hauteur. Le visage et le téléphone doivent rester dans la moitié haute du cadre.

```text
A confident West African man in his early thirties, short tapered fade and neat beard, sits sideways inside a large rounded arch-shaped niche carved into a cobalt blue #0866FF studio wall, the inside of the niche lit softly in sky blue #BFD6FF. He holds his smartphone in front of him at chest height, recording a short coaching video, mid-sentence with a warm, assured smile, one hand gesturing gently. He wears a navy #10244A heavy knit crewneck sweater over off-white trousers and clean white sneakers. Minimal set, nothing else in the frame. Vertical 4:5, his face and phone in the upper half of the frame.
```

### 3. La commerçante : carte « Cotonou », et chapitre Conviction d'À propos
**Fichier :** `usage-cotonou.webp` · **Décor :** le ciel · **Format :** 4:5, 3 000 × 3 750 px.

- **Usage :** affichée dans une arche verticale sur À propos (le haut du cadre compte) et en bandeau sur l'accueil. Le visage doit être un peu au-dessus du centre.

```text
Low-angle shot of a West African businesswoman in her forties against a pure, cloudless deep blue sky, looking down at her smartphone with a quiet, proud smile. She wears an elegant pale sky blue headwrap tied high and a cream ribbed knit turtleneck, small gold earrings, a few thin gold bangles. She holds the phone with both hands at chest height, phone case matte white. Soft late-morning sunlight from the left, gentle shadow on the face. Vertical 4:5, her face slightly above the center, sky filling the background, nothing else in the frame.
```

### 4. La formatrice : carte « Dakar » des avis
**Fichier :** `usage-dakar.webp` · **Décor :** atelier, devant l'arche · **Format :** 4:5, 3 000 × 3 750 px.

- **Usage :** recadré en bandeau 16:10. Le visage doit être dans le tiers supérieur, l'ordinateur dans le tiers bas.

```text
A young Senegalese woman in her mid-twenties with short natural coily hair and thin gold glasses sits cross-legged on a low white bench in front of a large cobalt blue #0866FF arch painted on a pale blue #EDF4FF studio wall. A light silver laptop rests on her knees, she types with one hand and smiles, looking up past the camera as if answering a student in a live class. She wears an oversized white chunky knit sweater and pale blue wide trousers. Minimal set, soft daylight from the left. Vertical 4:5, face in the upper third, laptop in the lower third, generous empty space around her.
```

### 5. Les mains : section Paiements de l'accueil
**Fichier :** `mains.webp` · **Décor :** fond uni bleu très pâle · **Format :** 1:1, 3 000 × 3 000 px.

- **Usage :** l'image occupe les deux tiers droits de la section, et le formulaire de paiement passe par-dessus sa partie gauche. Le téléphone doit donc être **à droite du centre**.
- **Écran :** il doit être blanc et vide. J'y incruste ensuite le vrai écran de paiement mepaye.

```text
Close-up of a dark-skinned hand holding a smartphone tilted toward the camera, relaxed natural grip, short clean nails, a few thin gold rings and a slim gold bangle, the cuff of a soft sky blue #BFD6FF chunky knit sweater visible at the wrist. The phone has a matte cobalt blue case and a plain white blank screen. Seamless pale blue #EDF4FF background, soft shadow of the hand. Square 1:1, the phone placed right of center at mid-height, empty space on the left half.
```

### 6. En plus, pour plus tard : la communauté
**Usage possible :** remplacer l'illustration « famille » d'À propos, ou servir à une page Affiliation. **Décor :** le ciel · **Format :** 3:2, 4 500 × 3 000 px.

```text
Low-angle shot of two West African creators in their twenties against a pure cloudless blue sky, laughing as they lean toward each other to compare their phones, one with long braids in a pale blue knit sweater, the other with a short afro in a cream ribbed cardigan. Matte white and cobalt blue phone cases. Bright soft sunlight, natural joy, candid moment. Horizontal 3:2, both faces in the upper half, plenty of sky around them.
```

---

## 6. Me les envoyer

1. Déposez les images retenues dans un dossier `photos-a-trier/` à la racine du projet, nommées comme ci-dessus (`creatrice`, `usage-abidjan`, `usage-cotonou`, `usage-dakar`, `mains`).
2. Dites-moi qu'elles y sont. Je m'occupe de la suite :
   - je détoure la créatrice et je recadre chaque image pour son emplacement ;
   - j'incruste l'écran de paiement mepaye dans le téléphone des mains ;
   - j'harmonise l'étalonnage de la série, je convertis en WebP et je remplace partout.
3. Avant de remplacer quoi que ce soit, je vous montre chaque image intégrée, sur ordinateur et sur mobile.
