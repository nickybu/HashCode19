from .model import Image

def parse_dataset(filename):
    with open(filename) as f:
        f.readline() # Discard the first line
        images = [_parse_image(line) for line in f.readlines()]

    return images

def _parse_image(line):
    tokens = line.split()

    orientation = tokens[0]
    images = tokens[2:]
    return Image(orientation, images)

