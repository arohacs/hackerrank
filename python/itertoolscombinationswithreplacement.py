#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

if __name__ == '__main__':
    # break input into list of size and string
    mystringlist = [ str(x) for x in input().split(' ')]
    # break string into list
    mystringsplit = sorted([x for x in mystringlist[0]])
    # get number of combination/replacements from string list
    size = int(mystringlist[1])
    # initialize list to store combos/replacements
    thelist = []
    # loop over combo/replacement size and populate list of raw results
    for i in range(1, size + 1):
        thelist.append(list(combinations_with_replacement(mystringsplit, i)))
    # initialize list for parsed results
    parsedlist = []
    # initialize the string counter used for sorting each list item alphabetically
    appstring = ''
    for i in thelist:
        # loop over each list item and sort
        for j in range(0, len(i)):
            # if list item matches the size
            if len(i[j]) == size:
                # sort and increment the string counter
                for k in range(0, len(i[j])):
                    appstring += str(i[j][k])
            # append if item is not an empty string
            if appstring != '':
                parsedlist.append(appstring)
            # reset string counter for the next loop
            appstring = ''
    # sort all of the items in order to print out the list in lexographic order
    sortedlist = sorted(parsedlist, key=lambda x: (len(x), x))
    # print the list to fulfill the STDOUT requirement of the exercise
    for i in sortedlist:
        print(i)
