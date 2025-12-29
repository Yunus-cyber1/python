# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 10:11:06 2025

@author: user
"""

print("Muzeyga Kirish. Dasturni toxtatmoqchibolsangiz exit yoki quit deb yozing")
while True:
    yosh=(input('Yoshingiz nechida>> '))
    if int(yosh)<7:
        print('Kirish narxi 2000 som')
    elif int(yosh)<18:
        print('Kirish narxi 3000 som')
    elif int(yosh)<65:
        print('Kirish narxi 10000 som')
    elif yosh=='quit' or yosh=='exit':
        break
    else :
        print('Sizga kirish bepul')