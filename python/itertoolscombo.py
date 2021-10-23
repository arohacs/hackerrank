#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations

if __name__ == '__main__':
    mystringlist = input()
    # split input to 2 list items: the string and the number of combinations
    mystringlist = mystringlist.split(' ')
    # split the string into its own list with one item
    mystring = [str(x) for x in mystringlist[0].split(' ')]
    # split into list of string letters
    mystringsplit = sorted([x for x in mystring[0]])
    # get combo list item
    size = int(mystringlist[1])
    # initialize list to append combo items
    thelist = []
    # create list of combo items
    for i in range(1, size + 1):
        thelist.append(list(combinations(mystringsplit, i)))
    # initialize list that will hold cleaned up list items
    thenewlist = []
    # initialize variable to hold each list item as it is stripped
    appstring = ''
    # loop through list, strip symbols, create appstring variable to append to thenewlist
    for i in thelist:
        for j in range(0, len(i)):
            if len(i[j]) == 1:
                thenewlist.append(str(i[j]).strip(",{}'()"))
                appstring = ''
                continue
            elif len(i[j]) > 1:
                for k in range(0, len(i[j])):
                    appstring += str(i[j][k])
            thenewlist.append(appstring)
            appstring = ''
            continue
    # sort the list
    thenewlist = sorted(thenewlist, key=lambda x: (len(x), x))
    # print the list
    for i in thenewlist:
        print(f'{i}')
