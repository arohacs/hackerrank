
#!/bin/python3

import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/py-if-else/problem

if __name__ == '__main__':
    n = int(input().strip())

if n % 2 > 0:
    # n is odd
    print("Weird")
elif n >= 2 and n <=5 and n % 2 == 0:
    print("Not Weird")
elif n >= 6 and n <= 20 and n % 2 == 0:
    print("Weird")
elif n > 20 and n % 2 == 0:
    print("Not Weird")
