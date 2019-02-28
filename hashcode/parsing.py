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

def compute_score(slides):
    score = 0
    for index, slide in enumerate(slides[:-1]):
        slide1_tags = slide.tags
        slide2_tags = (slides[index+1]).tags
        
        num_common_tags = list(set(slide1_tags).intersection(set(slide2_tags)))
        diff_s1_s2 = list(set(slide1_tags).difference(set(slide2_tags)))
        diff_s2_s1 = list(set(slide2_tags).difference(set(slide1_tags)))
        score += min(len(num_common_tags), len(diff_s1_s2), len(diff_s2_s1))
    return score
