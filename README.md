# Projet INN - Synthèse de Textures

Ce référentiel GitHub propose une implémentation de l'article "Texture Synthesis with Spatial Generative Adversarial Networks" ([PSGAN](https://arxiv.org/abs/1705.06566)) ainsi qu'une comparaison entre la génération de textures avec PSGAN et la méthode "Collage and Paste".

Le code de PSGAN est adapté à partir du référentiel suivant : [Zalando Research - Famos](https://github.com/zalandoresearch/famos/tree/master).

## Utilisation de PSGAN

Pour générer des textures avec PSGAN, utilisez la commande suivante :

```bash
python PSGAN.py --texturePath=samples/milano/ --ngf=120 --zLoc=50 --ndf=120 --nDep=5 --nDepD=5 --batchSize=16
```

## Méthode "copier-coller" pour la Génération de Textures

Nous avons également implémenté une méthode simple de génération de textures avec du copier-coller. Cette méthode consiste à découper des morceaux de la texture d'origine et à les coller de manière aléatoire pour créer une nouvelle texture.
