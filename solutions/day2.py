# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 15:43:34 2021

@author: gusta
"""

with open('pos.txt') as f:
    pos = f.readlines()
    
n = len(pos)

for i in range(n):
    pos[i] = pos[i].replace("\n", "").split(" ")
    pos[i][1] = int(pos[i][1])
    

# first
dep = 0
leng = 0


for i in range(n):
    if pos[i][0] == 'forward':
        leng += pos[i][1]
    elif pos[i][0] == 'down':
        dep += pos[i][1]
    elif pos[i][0] == 'up':
        dep -= pos[i][1]
    else:
        print("wrong input")
print("1: " + str(dep*leng))


# second
dep = 0
leng = 0
aim = 0

for i in range(n):
    if pos[i][0] == 'forward':
        leng += pos[i][1]
        dep += (aim*pos[i][1])
    elif pos[i][0] == 'down':
        aim += pos[i][1]
    elif pos[i][0] == 'up':
        aim -= pos[i][1]
    else:
        print("wrong input")

print("2: " + str(dep*leng))