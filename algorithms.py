"""
This module contains sorting algorithms:
Selection sort, Insertion sort, Merge sort, Shellsort.
"""

def selection_sort(lst: list) -> int:
    """Selection sort implementation. Returns a number of comparison operations."""
    compars = 0
    length = len(lst)
    for i in range(length):
        min_pos = i
        for j in range(i+1, length):
            compars += 1
            if lst[j] < lst[min_pos]:
                min_pos = j
        lst[i], lst[min_pos] = lst[min_pos], lst[i]
    return compars


def insertion_sort(lst: list) -> int:
    """Insertion sort implementation. Returns a number of comparison operations."""
    compars = 0
    length = len(lst)
    for i in range(1, length):
        for j in range(i, 0, -1):
            compars += 1
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:
                break
    return compars


def shellsort(lst: list) -> int:
    """Shellsort implementation. Returns a number of comparison operations."""
    compars = 0
    length = len(lst)
    h = 1
    while h < length / 3:
        h = 3 * h + 1
    while h >= 1:
        for i in range(h, length):
            j = i
            while j >= h:
                compars += 1
                if lst[j] < lst[j-h]:
                    lst[j], lst[j-h] = lst[j-h], lst[j]
                else:
                    break
                j -= h
        h = h // 3
    return compars


def merge_sort(lst) -> int:
    """Mergesort implementation with the use of recursion.
    Returns a number of comparison operations."""
    compars = 0
    length = len(lst)
    if length > 1:
        mid = length // 2
        left = lst[:mid]
        right = lst[mid:]
        compars_left = merge_sort(left)
        compars_right = merge_sort(right)
        compars += compars_left + compars_right
        i = j = 0
        while i < len(left) and j < len(right):
            compars += 1
            if left[i] < right[j]:
                lst[i+j] = left[i]
                i += 1
            else:
                lst[i+j] = right[j]
                j += 1
        while i < len(left):
            lst[i+j] = left[i]
            i += 1
        while j < len(right):
            lst[i+j] = right[j]
            j += 1
    return compars
