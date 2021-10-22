#!/usr/bin/env python3

#  https://www.hackerrank.com/challenges/itertools-permutations/problem
from itertools import permutations

if __name__ == '__main__':

    mystringlist = input()
    mystringlist = mystringlist.split(' ')
    mystring = [str(x) for x in mystringlist[0]]
    perms = int(mystringlist[1])
    thelist = list(permutations(mystring, perms))
    thenewlist = []
    appstring = ''
    for i in thelist:
        for j in range(0,len(i)):
            appstring += i[int(j)]
            if j == perms - 1:
                print(f'j = {j}, breaking')
                thenewlist.append(appstring)
                appstring = ''
                continue
    thenewlist = sorted(thenewlist)
    for i in thenewlist:
        print(i)

