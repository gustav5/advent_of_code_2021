# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 07:54:36 2021

@author: gusta
"""
#fixing textfile
with open('chunks.txt') as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n","")
    
#creating some dictionaries 
dict1 = {")": 3,"]": 57 , "}": 1197, ">": 25137}
pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
pairs2 = {"(":")" ,"[" : "]", "{":"}" ,  "<" :">"}
score = {")": 1,"]": 2 , "}": 3, ">": 4}


#first
sum1 = 0
li1 = []
corrupted = set()
for i in range(len(lines)):
    for letter in lines[i]:
        if letter == ")" or letter == "]" or letter == "}" or letter == ">":
            if li1.pop() != pairs[letter]:
                sum1 += dict1[letter]
                corrupted.add(i)
                break
        else:
            li1.append(letter)
print(sum1)


#second
# make a new file without the corrupted lines
new_lines = []
for i in range(len(lines)):
    if i not in corrupted:
        new_lines.append(lines[i])

# get the incomplete ones
missing = []
for i in range(len(new_lines)):
    li1 = []
    for letter in new_lines[i]:
        if letter == ")" or letter == "]" or letter == "}" or letter == ">":
            li1.pop() #this will leave only the ones missing left
        else:
            li1.append(letter)
    li1.reverse()
    missing.append(li1)

# calculating the score
score_list = []
for i in range(len(missing)):
    sum2 = 0
    for j in range(len(missing[i])):
        sum2 = 5*sum2 + score[pairs2[missing[i][j]]]
    score_list.append(sum2)
            
#get middle score by sorting and picking middle
print(sorted(score_list)[int(len(score_list)/2)])



      
        