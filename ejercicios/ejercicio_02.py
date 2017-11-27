#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio

Instrucciones

	1. Ordenar la siguiente lista de valores por medio de ciclos y/o validaciones
	arreglo = [43, 58, 54,  4,  3, 50, 12, 61, 67, 91, 70, 34, 76, 20, 75,  0, 24,
       98, 70, 17, 95, 13, 92, 45, 54, 83, 51, 55, 97, 73, 49, 36, 86, 40,
       61, 89,  4, 87, 98, 35,  5, 77, 18, 46, 89,  2, 72, 47, 33, 44]
    Resultado
    arreglo = [0,  2,  3,  4,  4,  5, 12, 13, 17, 18, 20, 24, 33, 34, 35, 36, 40,
       43, 44, 45, 46, 47, 49, 50, 51, 54, 54, 55, 58, 61, 61, 67, 70, 70,
       72, 73, 75, 76, 77, 83, 86, 87, 89, 89, 91, 92, 95, 97, 98, 98]  
"""

a = [43, 58, 54, 4, 3, 50, 12, 61, 67, 91, 70, 34, 76, 20, 75, 0, 24, 98, 70, 17, 95, 13, 92, 45, 54, 83, 51, 55, 97, 73, 49, 36, 86, 40, 61, 89,  4, 87, 98, 35,  5, 77, 18, 46, 89, 2, 72, 47, 33, 44]

def bubbleSort(a):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)