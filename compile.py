import png
import os

from config import *


def load_layers():
    layers = {}

    for layer_name, path in LAYER_PATHS.items():
        for filename in os.listdir(path):
            png_path = os.path.join(path, filename)
            if os.path.isfile(png_path):
                png_file = png.Reader(filename=png_path)
                png_file.read()
                layers[layer_name] = png_file
    return layers


layers = load_layers()
print(layers)
