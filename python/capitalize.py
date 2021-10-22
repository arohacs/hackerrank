#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    names=s.split(" ")
    fullname = ''
    for i in names:
        for j in range(len(i)):
            if j == 0:
                fullname += i[0].upper()
            else:
                fullname += i[j] 
        fullname += ' '
    return fullname
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
