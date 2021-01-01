#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:31:13 2019

@author: chansa
"""


def merge_sort(dataset):
    # we Split array into half

    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarray = dataset[:mid]
        rightarray = dataset[mid:]

# TODO: recursively break down the arrays
        merge_sort(leftarray)
        merge_sort(rightarray)


# TODO: perform the merging
        i = 0
        j = 0
        k = 0


# TODO while both arrays have content
        while i < len(leftarray) and j < len(rightarray):
            if leftarray[i] < rightarray[j]:
                dataset[k] = leftarray[i]
                i += 1
            else:
                rightarray[j] < leftarray[i]
                dataset[k] = rightarray[j]
                j += 1
            k += 1


# TODO: if left array still has values
        while i < len(leftarray):
            dataset[k] = leftarray[i]
            i += 1
            k += 1

# TODO: if right array still has values

        while j < len(rightarray):
            dataset[k] = rightarray[j]
            j += 1
            k += 1


# TODo: test the merge_sort
items = [1, 5, 9]
merge_sort(items)
print(items)

