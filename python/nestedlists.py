#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    mylist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mylist.append([name,score])
    list = sorted(mylist, key = lambda x:float(x[:][1]))
mylist = sorted(mylist, key = lambda x:float(x[1]))
listlen = len(mylist)
lowestscoreindex = 0
secondlowestscoreindex = 0
names = []
for index, namescore in enumerate(mylist):
    if index == listlen -1:
        pass
    elif index == 0: # if we are on the first item
        for _ in range(listlen -1):
            if namescore[1] == mylist[_ + 1][1]:
                lowestscoreindex = _ + 1

secondlowestscoreindex = lowestscoreindex + 1

secondlowestscore = mylist[secondlowestscoreindex][1]

for _ in range(secondlowestscoreindex, len(mylist)):
    if mylist[_][1] == secondlowestscore:
        names.append(mylist[_][0])
names = sorted(names)
for i in names:
    print(i)

