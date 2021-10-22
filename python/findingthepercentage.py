#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
sum = 0
for _ in student_marks[query_name]:
    sum += _
sum = sum / len(student_marks[query_name])       
print(f'{sum:.2f}'
