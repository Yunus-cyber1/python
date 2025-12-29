# -*- coding: utf-8 -*-
"""
Created on Sat Dec 27 19:48:19 2025

@author: user
"""

olim0={'ism':'Nyuton', 'yil':1884, 'shahar':'fransiya','umr':54}
olim1={'ism':'Arximed', 'yil':225, 'shahar':'gresiya','umr':87}
olim2={'ism':'Ilon Mask', 'yil':1996, 'shahar':'amerika','umr':78}
olimlar=[olim0,olim1,olim2]

    
olim0['asar']=['fizika asoslari','fizika qonunlari']
olim1['asar']=['arximed qonuni','davlat boshqarish sirlari']
olim2['asar']=['marsni egallash','raketa qurish','spaceX']
for olim in olimlar:
    print(f"{olim['ism']} quyidagi kitoblarni yozgan:\n>>>>", end='')
    for a in olim['asar']:
        print(a)