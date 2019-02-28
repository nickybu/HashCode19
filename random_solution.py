from random import shuffle
import sys

from hashcode.parsing import parse_dataset, print_solution
from hashcode.model import *

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
    vertical_images = filter(lambda x: x.orientation == 'vertical', images)
    shuffle(vertical_images)
    
    if len(vertical_images) % 2 != 0:
        vertical_images = vertical_images[:-1]

    grouped = list(zip(*[iter(vertical_images)] * 2))
    return [VerticalSlide(left, right) for left, right in grouped]


horizontal_slides = [HorizontalSlide(i) for i in horizontal_images]
vertical_slides = rand_vertical_slides(images)

print_solution(horizontal_slides + vertical_slides)

