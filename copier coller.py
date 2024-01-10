from PIL import Image, ImageDraw
import numpy as np
import random
import matplotlib.pyplot as plt
import os

def extract_patches(image, patch_size, overlap):
    """Extrait des patches de l'image source."""
    patches = []
    img_width, img_height = image.size
    for i in range(0, img_height - patch_size + 1, patch_size - overlap):
        for j in range(0, img_width - patch_size + 1, patch_size - overlap):
            patch = image.crop((j, i, j + patch_size, i + patch_size))
            patches.append(patch)
    return patches

def calculate_ssd(patch, target_region):
    """Calcule la somme des différences au carré (SSD) entre un patch et une région cible."""
    patch_np = np.array(patch)
    target_np = np.array(target_region)
    return np.sum((patch_np - target_np) ** 2)

def find_best_patch(patches, target_region, overlap):
    """Trouve le meilleur patch pour la région cible."""
    min_ssd = float('inf')
    best_patch = None
    for patch in patches:
        ssd = calculate_ssd(patch.crop((0, 0, patch.size[0], overlap)), target_region.crop((0, 0, target_region.size[0], overlap))) if overlap else calculate_ssd(patch, target_region)
        if ssd < min_ssd:
            min_ssd = ssd
            best_patch = patch
    return best_patch

def texture_synthesis(source_image, target_height, target_width, patch_size, overlap):
    """Synthétise une nouvelle texture à partir de l'image source."""
    target_image = Image.new('RGB', (target_width, target_height))
    patches = extract_patches(source_image, patch_size, overlap)
    for i in range(0, target_height, patch_size - overlap):
        for j in range(0, target_width, patch_size - overlap):
            if i == 0 and j == 0:
                target_image.paste(random.choice(patches), (j, i))
            else:
                target_region = target_image.crop((j, i, j + patch_size, i + patch_size))
                best_patch = find_best_patch(patches, target_region, overlap)
                target_image.paste(best_patch, (j, i))
    return target_image

def draw_grid(image, patch_size, overlap):
    """Dessine une grille sur l'image pour montrer comment elle est divisée en patches."""
    draw = ImageDraw.Draw(image)
    img_width, img_height = image.size
    for i in range(0, img_height - patch_size+1, patch_size - overlap):
        for j in range(0, img_width - patch_size+1, patch_size - overlap):
            draw.rectangle([j, i, j + patch_size, i + patch_size], outline="red")
    return image

# Paramètres
source_image_path = r'\samples\milano\m1.png'
patch_size = 60  
overlap = 20    

source_image = Image.open(source_image_path).resize((600,600))

# Affichage de l'image source redimensionnée 
print("Taille de l'image source redimensionnée :", source_image.size)
print(extract_patches(source_image, patch_size, overlap)[0])

# Synthèse de la texture
synthesized_texture = texture_synthesis(source_image, 300, 300, patch_size, overlap)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(source_image)
plt.title("Image Source")
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(synthesized_texture)
plt.title("Texture Synthétisée")
plt.axis('off')
plt.show()
