from collections import defaultdict
from random import shuffle
import signal
import sys

from hashcode.parsing import *
from hashcode.model import *

max_solution = None
max_score = None

def exit_handler(sig, frame):
    global max_solution
    print_solution(solution)
    sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)

dataset = 'a'
if len(sys.argv) == 2:
    dataset = sys.argv[1]

datasets = {
    'a': 'datasets/a_example.txt',
    'b': 'datasets/b_lovely_landscapes.txt',
    'c': 'datasets/c_memorable_moments.txt',
    'd': 'datasets/d_pet_pictures.txt',
    'e': 'datasets/e_shiny_selfies.txt'
}

images = parse_dataset(datasets[dataset])

horizontal_images = filter(lambda x: x.orientation == 'horizontal', images)
vertical_images = filter(lambda x: x.orientation == 'vertical', images)

horizontal_slides = [HorizontalSlide(i) for i in horizontal_images]

def tag_frequencies(images):
    freqs = {}

    for image in images:
        for tag in image.tags:
            freqs[tag] = freqs.get(tag, 0) + 1

    return freqs

def tag_map(images):
    tag_map = defaultdict(list)
    for image in images:
        for tag in image.tags:
            tag_map[tag].append(image.id)

    return tag_map

def pair(images):
    images = filter(lambda x: x.orientation == 'vertical', images)

    freqs = tag_frequencies(images)
    imgs = tag_map(images)

    def val(image):
        tag_freq = [freqs[tag] for tag in image.tags]
        return max(tag_freq)

    images = sorted(images, key=val)

    slides = []
    while len(images) >= 2:
        slide = VerticalSlide(images[0], images[-1])
        del images[0]
        del images[-1]
        slides.append(slide)

    return slides

def sort_slides(images):
    freqs = tag_frequencies(images)
    imgs = tag_map(images)

    def val(image):
        tag_freq = [freqs[tag] for tag in image.tags]
        return max(tag_freq)

    images = sorted(images, key=val)
    return images


v_slides = pair(images)
h_slides = [HorizontalSlide(i) for i in horizontal_images]

slides = sort_slides(v_slides + h_slides)

print_solution(slides)

