# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 15:37:33 2021

@author: gusta
"""

with open('depth.txt') as f:
    lines = f.readlines()

#first
depth = []
for i in range(0,len(lines)):
    depth.append(int(lines[i].replace("\n", "")))
    
count = 0
for i in range(1,len(depth)):
    if depth[i-1] < depth[i]:
        count += 1
print("1: " + str(count))

#second
count = 0
n = len(depth)
first = (depth[0:3])
last = (depth[1:4])
for i in range(2,n-1):
    if sum(first) < sum(last):
        count += 1
    first = last
    last = depth[i:i+3]
print("2: " + str(count))