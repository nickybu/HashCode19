from sys import stdout

from .model import Image

def parse_dataset(filename):
    with open(filename) as f:
        f.readline() # Discard the first line
        images = [_parse_image(_id, line) for _id, line in enumerate(f.readlines())]

    return images

def print_solution(slides, outfile=stdout):
    print >> outfile, len(slides)
    for slide in slides:
        _print_slide(slide, outfile)

def _print_slide(slide, outfile=stdout):
    print >> outfile, " ".join([str(i.id) for i in slide.images])

def _parse_image(_id, line):
    tokens = line.split()

    orientation = tokens[0]
    images = tokens[2:]
    return Image(_id, orientation, images)

