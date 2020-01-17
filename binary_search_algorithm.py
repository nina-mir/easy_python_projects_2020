# Auhtor: Nina Mir
# Date: January 16 2020
# easy python project implementing binary search algorithm
# of a search term in a sorted array or list
import sys


def find_mean_index(low, high):
    mean_indx = int((low + high)/2)
    return mean_indx


def check_boundaries(low, high, target):
    flag = [False, None]
    if target == low:
        print('Found ')
        flag = [True, 'l']
    elif target == high:
        print('Found ')
        flag = [True, 'h']
    return flag


def main(search_term):
    # list to be searched;
    # it must be in an increasing sorted pattern already
    list = [-10, 0, 1, 2, 3, 5, 6, 7, 9, 90, 900, 903, 1009, 1034, 5000]

    low, high = 0, len(list) - 1
    setup = check_boundaries(list[low], list[high], search_term)
    flag = setup[0]

    while not flag:
        print("keep on searching ...")
        mean_index = find_mean_index(low, high)
        if (search_term > list[high]) | (search_term < list[low]):
            flag, setup[1] = True, True
        if not setup[1]:
            if list[mean_index] < search_term:
                low = mean_index
            elif list[mean_index] > search_term:
                high = mean_index
            elif list[mean_index] == search_term:
                flag = True
    else:
        if not setup[1]:
            print('found target number @ index:', mean_index)
        elif setup[1] == 'l':
            print('found target number @ index:', low)
        elif setup[1] == 'h':
            print('found target number @ index:', high)
        elif setup[1]:
            print('Not Found in this List!')


if __name__ == '__main__':
    main(int(sys.argv[1]))
