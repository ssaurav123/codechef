# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 12:59:39 2018

@author: shubham
"""
for _ in range(int(input())):
    n = input().strip()
    count = 0
    for i in range(len(n)):
        if n[i] != '4' and n[i] !='7':
            count+=1
    print(count)