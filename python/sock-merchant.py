

#!/bin/python3

import math
import os
import random
import re
import sys

#https://www.hackerrank.com/challenges/sock-merchant/problem


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here

    mypairs = {}
    pairs = 0

    for i in range(n):
        if ar[i] not in mypairs:
            mypairs[ar[i]] = 1
        else:
            mypairs[ar[i]] += 1

    for k,v in mypairs.items():
        pairs += v // 2

    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
