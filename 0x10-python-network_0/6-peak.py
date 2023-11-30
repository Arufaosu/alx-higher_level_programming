#!/usr/bin/python3

#  finds a peak in a list of unsorted integers
def find_peak(list_of_integers, low, high):
    if low == high:
        return list_of_integers[low]

    mid = (low + high) // 2

    if list_of_integers[mid] > list_of_integers[mid + 1]:
        return find_peak(list_of_integers, low, mid)
    else:
        return find_peak(list_of_integers, mid + 1, high)

def peak_finder(list_of_integers):
    if not list_of_integers:
        return None

    return find_peak(list_of_integers, 0, len(list_of_integers) - 1)

print(peak_finder([1, 2, 4, 6, 3]))
print(peak_finder([4, 2, 1, 2, 3, 1]))
print(peak_finder([2, 2, 2]))
print(peak_finder([]))
print(peak_finder([-2, -4, 2, 1]))
print(peak_finder([4, 2, 1, 2, 2, 2, 3, 1]))
