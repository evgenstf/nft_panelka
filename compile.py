from PIL import Image
import os

from config import *


def load_layers():
    layers = {}

    for layer_name, path in LAYER_PATHS.items():
        layers[layer_name] = []
        for filename in os.listdir(path):
            png_path = os.path.join(path, filename)
            if os.path.isfile(png_path):
                img = Image.open(png_path)
                layers[layer_name].append(img)
    return layers

def cartesian_product_paste(bases, items):
    result = []
    for base in bases:
        for item in items:
            new_base = base.copy()
            new_base.paste(item, (0, 0), item)
            result.append(new_base)
    return result



layers = load_layers()
print(layers)

outputs = layers['base']

for name, pngs in layers.items():
    if name == 'base':
        continue
    outputs = cartesian_product_paste(outputs, pngs)



id = 0
for output in outputs:
    filename = str(id) + '.png'
    file_path = OUTPUT + '/' + filename
    print('file_path:', file_path)
    output.save(file_path, "PNG")
    id += 1





"""


img = Image.open("data_mask_1354_2030.png")

print(img.size)

background = Image.open("background_730_1097.png")

print(background.size)

# resize the image
size = (1354,2030)
background = background.resize(size,Image.ANTIALIAS)

background.paste(img, (0, 0), img)
background.save('how_to_superimpose_two_images_02.png',"PNG")
"""
