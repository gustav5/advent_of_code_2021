# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:09:23 2021

@author: gusta
"""

nums = [90,4,2,96,46,1,62,97,3,52,7,35,50,28,31,37,74,26,59,53,82,47,83,80,19,40,68,95,34,55,54,73,12,78,30,63,57,93,72,77,56,91,23,67,64,79,85,84,76,10,58,0,29,13,94,20,32,25,11,38,89,21,98,92,42,27,14,99,24,75,86,51,22,48,9,33,49,18,70,8,87,61,39,16,66,71,5,69,15,43,88,45,6,81,60,36,44,17,41,65]


with open('tables.txt') as f:
    tables = f.readlines()
    
n = len(tables)

for i in range(n):
    tables[i] = tables[i].replace("\n", "")
    
    
# making a matrix
tab1 = []
inner_tab = []
for i in range(n):
    if len(tables[i]) != 0 :
        inner_tab.append(tables[i].split())
    if len(tables[i]) == 0 or i == n-1: #last case that second thing
        tab1.append(inner_tab)
        inner_tab = []
        
#make strings int
m = len(tab1)

for i in range(m):
    for j in range(5):
        for k in range(len(tab1[i][j])):
            tab1[i][j][k] = int(tab1[i][j][k])



#making some functions
def check_rows(mat):
    rows = len(mat)
    cols = len(mat[0])
    
    for i in range(rows):
        sum1 = 0
        for j in range(cols):
            sum1 += mat[i][j]
        if sum1 == -5:
            return True # winner
    return False # no win

def check_cols(mat):
    rows = len(mat)
    cols = len(mat[0])
    
    for j in range(cols):
        sum1 = 0
        for i in range(rows):
            sum1 += mat[i][j]
        if sum1 == -5:
            return True # winner
    return False # no win

def check_off(li, x): #if board has number, set it to -1
    n = len(li)
    rows = len(li[0])
    cols = len(li[0][0])
    
    for i in range(n):
        mat = li[i]
        
        for j in range(rows):
            for k in range(cols):
                if mat[j][k] == x:
                    mat[j][k] = -1
        li[i] = mat
    return li
    
def sum_of_board(mat):
    sum1 = 0
    rows = len(mat)
    cols = len(mat[0])
    
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] > 0:
                sum1 += mat[i][j]
    return sum1

tab2 = tab1
#first

for x in nums:
    winner = False
    n = len(tab1) 
    check_off(tab1, x)
    for i in range(n):
        #check if winner
        if check_cols(tab1[i]) or check_rows(tab1[i]):
            winner = True
            print("1: " + str(x*sum_of_board(tab1[i])))
            break
        else:
            pass
    if winner:
        break



#second
tab1 = tab2

def play_one_round(tab1,x):
    n = len(tab1) 

    winners = []
    check_off(tab1, x)
    for i in range(n):
        #check if winner
        if check_cols(tab1[i]) or check_rows(tab1[i]):
            #save winner id
            winners.append(i)
        else:
            pass        
    return winners



#play rounds until last
winners_set = set()
last_x = -1
last_winner = -1
for x in nums:
    if len(winners_set) == 100: #last winner
        print("2: " + str(sum_of_board(tab1[last_winner])*last_x))
        break
    winners = play_one_round(tab1,x)
    for i in range(len(winners)):
        if winners[i] not in winners_set:
            winners_set.add(winners[i])
            last_winner = i
            last_x = x
   








