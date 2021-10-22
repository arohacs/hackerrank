#!/usr/bin/env python3

"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and is times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.


Sample Input

9 27

Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

https://www.hackerrank.com/challenges/designer-door-mat/problem

"""

def printPattern(n):

    # split input into list and convert to integers
    dimlist = [int(x) for x in n.split(' ')]
    # print the dimensions
    vert = dimlist[0]
    horiz = dimlist[1]
    c = "-"
    halfhoriz = (dimlist[1] -3) // 2
    halfvert = (dimlist[0] // 2)
    dazzle = ".|."

    for i in range(1, vert,2):
        if i <= vert -2:
            print((dazzle * i).center(horiz,'-'))
        if i >= vert -2:
            print('WELCOME'.center(horiz,'-'))
    for i in range(vert -2,0, -2):
        print((dazzle * i).center(horiz,'-'))
#
if __name__ == '__main__':
    n = printPattern(input())
