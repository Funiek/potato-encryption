#!/usr/bin/python3
import sys
import numpy as np


def encrypt(value:str,key:str):
    column_count = len(key.split('-'))

    temp = int(len(value)/column_count)
    if(len(value)/column_count%1==0):
        rows_count = temp
    else:
        rows_count = temp+1

    #arr = [[0 for x in range(rows_count)] for y in range(column_count)]
    arr = [0]*rows_count
    arr = [arr]*column_count
    

    return arr


print(encrypt(sys.argv[1],sys.argv[2]))
