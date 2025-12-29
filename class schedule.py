# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 20:19:06 2025

@author: user
"""

schedule={}
day =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
for n in range(0,7):
    answer=input(f"Have you classes on {day[n]}")
    if answer=='yes':
        t=1
        lessons=[]
        while True:
            class1=input(f" What is your {t}-class?If you have no more classes write NO>>")
            if class1.upper()=='NO':
                break
            else:
                lessons.append(class1)
            t+=1    
        schedule[day[n]]=lessons      
for keys,qiymat in schedule.items():
    print (f"{keys}:{qiymat}")
