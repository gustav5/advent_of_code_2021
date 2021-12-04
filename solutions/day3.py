# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 07:58:28 2021

@author: gusta
"""



with open('bit_data.txt') as f:
    bits = f.readlines()
    
li = []
for i in range(len(bits)):
    li.append(bits[i][0:12])
n = len(li)
m = len(li[0])
    

# first

#create counter

gamma = [] # most common
epsilon = [] # least common

for i in range(0,12):
    gamma.append({"0" : 0, "1" : 0})
    epsilon.append({"0" : 0, "1" : 0})
    
n = len(li)
m = len(li[1])
    
count = 0
for i in range(n):
    for j in range(m):
        if li[i][j] == "1":
            gamma[j]["1"] += 1
        if li[i][j] == "0":
            gamma[j]["0"] += 1
    count += 1




most = ""
for i in range(m):
    if gamma[i]["0"] > gamma[i]["1"]:
        most += "0"
    else:
        most += "1"

least = most.replace("1","_").replace("0","1").replace("_","0") # invert binary number


print("1: " + str(int(most, 2)*int(least,2)))



#second


#create counter

gamma = [] # most common
epsilon = [] # least common

for i in range(0,12):
    gamma.append({"0" : 0, "1" : 0})
    epsilon.append({"0" : 0, "1" : 0})



def most_common(li,j):
    n = len(li)
    ones = 0
    zeroes = 0
    for i in range(n):
        if li[i][j] == "1":
            ones += 1
        elif li[i][j] == "0":
            zeroes += 1
            
    if ones >= zeroes:
        return "1"
    else:
        return "0"
    
def least_common(li,j):
    n = len(li)
    ones =0
    zeroes = 0
    for i in range(n):
        if li[i][j] == "1":
            ones += 1
        elif li[i][j] == "0":
            zeroes += 1
            
    if zeroes <= ones:
        return "0"
    else:
        return "1"    


    
########## most common
li1 = li
li2 = []
for j in range(m):
    cur = most_common(li1,j)
    for i in range(len(li1)):
        if li1[i][j] == cur:
            li2.append(li1[i])
    if len(li2) == 1:
        break
    li1 = li2
    li2 = []


a = li2[0]


#least common
li1 = li
li2 = []
for j in range(m):
    cur = least_common(li1,j)
    for i in range(len(li1)):
        if li1[i][j] == cur:
            li2.append(li1[i])
    if len(li2) == 1:
        break
    li1 = li2
    li2 = []

    
b = li2[0]

    
print("2: " + str(int(a, 2)*int(b,2)))
    