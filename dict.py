import hashcode.parsing as parse
from collections import defaultdict


def get_dic(d):
    dic = defaultdict(set)

    count = 0
    for im in d:
        for tag in im.tags:
            dic[tag].add(count)
        count += 1

    return dic

def most_common(lst):
    return max(set(lst), key=lst.count)

datasets = {
    'a': 'datasets/a_example.txt',
    'b': 'datasets/b_lovely_landscapes.txt',
    'c': 'datasets/c_memorable_moments.txt',
    'd': 'datasets/d_pet_pictures.txt',
    'e': 'datasets/e_shiny_selfies.txt'
}

d = parse.parse_dataset(datasets['a'])

# slides = []
# slides.append(d[0])
# d.remove(d[0])
#
# dic = get_dic(d)
# no_list = []
#
# count = 0
# while len(d) > 0:
#     ids = []
#
#     for tag in slides[len(slides) - 1].tags:
#         for p_id in dic[tag]:
#             if d[p_id] not in no_list:
#                 ids.append(p_id)
#
#     print('ids = ', ids)
#     if len(ids) == 0:
#         for im in d:
#             if im not in no_list:
#                 candidate = im
#                 no_list.append(im)
#                 slides.append(candidate)
#                 break
#     else:
#         m_id = most_common(ids)
#         candidate = d[m_id]
#         no_list.append(candidate)
#
#         count +=1
#         print(count, '->', candidate)
#         slides.append(candidate)
#
#     if candidate.orientation == 'vertical' and len(d) > 0:
#         for im in d:
#             if im.orientation == 'vertical' and im not in no_list:
#                 slides.append(im)
#                 no_list.append(im)
#                 break


parse.print_solution(d, 'solutions/b.txt')