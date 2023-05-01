#!/usr/bin/python3
""" A function that finds a peak in a list of unsorted integers. """

def find_peak(list_of_integers):
    if list_of_integers == []:
        return None

    enu = len(list_of_integers)
    etiti = int(enu / 2)
    ani = list_of_integers

    if etiti - 1 < 0 and etiti + 1 >= enu:
        return ani[etiti]
    elif etiti - 1 < 0:
        return ani[etiti] if ani[etiti] > ani[etiti + 1] else ani[etiti + 1]
    elif etiti + 1 >= enu:
        return ani[etiti] if ani[etiti] > ani[etiti - 1] else ani[etiti - 1]

    if ani[etiti - 1] < ani[etiti] > ani[etiti + 1]:
        return li[mid]

    if ani[etiti + 1] > ani[etiti - 1]:
        return find_peak(ani[etiti:])
    return find_peak(ani[:etiti])
