# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:46:39 2020

@author: Admin
"""

a=[]
for i in range(9):
    a.append([])
for i in range(9):
    for j in range(9):
        if j==4 and i>2:
            a[i].append('  ')
        else:
            a[i].append(' ')
n=0
num=1
down_start=4
up_start=5
down_end=5
up_end=2
value=False
for z in range(3):
    for i in range(down_start,down_end,2):
        for j in range(n,n+1):
            a[i][j]=num
        num+=1
        if num>13 or value:
            num-=2
            value=True
    n+=1
    if n==5:
        up_start-=2
        up_end+=2
        down_start+=2
        down_end-=2
        break
    for i in range(up_start,up_end,-2):
        for j in range(n,n+1):
            a[i][j]=num
        num+=1
    n+=1
    down_start-=2
    up_start+=2
    down_end+=2
    up_end-=2

for z in range(2):
    for i in range(up_start,up_end,-2):
        for j in range(n,n+1):
            a[i][j]=num
        num-=1
    n+=1
    for i in range(down_start,down_end,2):
        for j in range(n,n+1):
            a[i][j]=num
        num-=1
    n+=1
    up_start-=2
    up_end+=2
    down_start+=2
    down_end-=2
for i in range(9):
    for j in range(9):
        print(a[i][j],end=' ')   
    print()         
            
            
    
        