#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    maxbin = bin(number)[2:]
    binlen = len(maxbin)
    for i in range(1, n + 1):
        bini = bin(i)[2:]
        octi = oct(i)[2:]
        hexi = hex(i)[2:].upper()
        print(f'{str(i).rjust(binlen)} {octi.rjust(binlen)} {hexi.rjust(binlen)} {bini.rjust(binlen)}')
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

