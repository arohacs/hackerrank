#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
runlist = []
splitlist = []
mylist = []
thecommand = ''
for item in range(N):
    runlist.append(input())
for item in runlist:    
    eachlist = str(item).split(' ')
    if len(eachlist) > 1:
        newlist = [eachlist[0], [int(x) for x in eachlist[1:]]]
        splitlist.append(newlist)
    elif len(eachlist) == 1:
        splitlist.append(eachlist)

for index in splitlist:
    if len(index) == 1:
        if index[0] == "print":
            print(mylist)
        elif index[0] == "sort":
            mylist.sort()
        elif index[0] == "pop":
            mylist.pop()
        elif index[0] == "reverse":
            mylist.reverse()
    elif len(index) > 1:
        if index[0] == "insert":
            mylist.insert(index[1][0], index[1][1])
        elif index[0] == "remove":
            mylist.remove(index[1][0])
        elif index[0] == "append":
            mylist.append(index[1][0])
