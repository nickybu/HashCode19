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
vertical_image = filter(lambda x: x.orientation == 'vertical', images)

def rand_vertical_slides(images):
    vertical_images = list(filter(lambda x: x.orientation == 'vertical', images))
    shuffle(vertical_images)
    
    if len(vertical_images) % 2 != 0:
        vertical_images = vertical_images[:-1]

    grouped = list(zip(*[iter(vertical_images)] * 2))
    return [VerticalSlide(left, right) for left, right in grouped]


while True:
    horizontal_slides = [HorizontalSlide(i) for i in horizontal_images]
    vertical_slides = rand_vertical_slides(images)

    solution = horizontal_slides + vertical_slides
    score = compute_score(solution)

    if max_score == None or score > max_score:
        max_solution = solution
        max_score = score
        print >> sys.stderr, score


