#!/usr/bin/env python3

#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    myset = set(array)
    result = f'{sum(myset)/len(myset):.3f}'
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


