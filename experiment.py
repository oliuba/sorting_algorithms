"""This module contains experiments for sorting algorithms comparison."""

from random import random, randint, shuffle
from time import time
from copy import copy
from math import ceil
from algorithms import selection_sort, insertion_sort, shellsort, merge_sort

ALGOS = {'Selection sort': selection_sort, 'Insertion sort': insertion_sort, \
    'Shellsort': shellsort, 'Merge sort': merge_sort}


def generate_random_list(power: int) -> list:
    """Generates a list of size 2^power with random numbers and returns it."""
    lst = []
    for _ in range(2 ** power):
        lst.append(random())
    return lst


def generate_sorted(power: int) -> list:
    """Generates a list of size 2^power with random numbers
    sorted from lower to higher and returns it."""
    lst = generate_random_list(power)
    return sorted(lst)


def generate_sorted_reverse(power: int) -> list:
    """Generates a list of size 2^power with random numbers
    sorted from higher to lower and returns it."""
    lst = generate_random_list(power)
    return sorted(lst, reverse=True)


def generate_repeated(power: int) -> list:
    """Generates a list of size 2^power with numbers from set {1, 2, 3}."""
    lst = []
    for _ in range(2 ** power):
        lst.append(randint(1, 3))
    return lst


def experiment(func, filename: str, exp_num: int):
    """Experiment simulation for one of list data: random, sorted, reversed, repeated.
    Writes the results to separate files."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('Size, Algorithm name, Comparisons, Working time\n')
    for power in range(7, 16):
        algo_times = {'Selection sort': 0, 'Insertion sort': 0, \
    'Shellsort': 0, 'Merge sort': 0}
        algo_comps = {'Selection sort': 0, 'Insertion sort': 0, \
    'Shellsort': 0, 'Merge sort': 0}
        for i in range(exp_num):
            if func == generate_repeated:
                if i == 0:
                    lst = func(power)
                else:
                    shuffle(lst)
            else:
                lst = func(power)
            for alg in ALGOS:
                to_sort = copy(lst)
                start = time()
                comps = ALGOS[alg](to_sort) # list is sorted here
                end = time()
                algo_times[alg] += (end - start)
                algo_comps[alg] += comps
        with open(filename, 'a', encoding='utf-8') as data_f:
            for alg in ALGOS:
                data_f.write(f'2^{power}, {alg}, {ceil(algo_comps[alg] / exp_num)}, {(algo_times[alg] / exp_num)}\n')


INPUT_DATA = {'Random numbers1': (generate_random_list, 5), 'Sorted numbers1': \
    (generate_sorted, 1), 'Reversed sorted numbers1': (generate_sorted_reverse, 1), \
        'Numbers 1-31': (generate_repeated, 3)}


def main_exp():
    """Main experiment that combines experiments for each type of input data."""
    for exp in INPUT_DATA:
        filename = exp + '.csv'
        func = INPUT_DATA[exp][0]
        exp_num = INPUT_DATA[exp][1]
        experiment(func, filename, exp_num)

main_exp()
