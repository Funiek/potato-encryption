#!/usr/bin/python3
import sys

def encrypt_decrypt(value:str,key:str):
    key_arr = key.split('-')
    
    #specifying dimensions
    column_count = len(key_arr)
    
    temp = int(len(value)/column_count)
    if(len(value)/column_count%1==0):
        rows_count = temp
    else:
        rows_count = temp+1

    print(str(rows_count)+" "+str(column_count))

    #2D matrix declaration
    inf = float('inf')
    arr = [[inf for x in range(column_count)] for y in range(rows_count)]
    

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in arr]))
    
    #filling matrix with data from value
    row=0
    col=0
    print("LENGTH OF VALUE: "+str(len(value)))
    for x in range(len(value)):
        print("X: "+str(x)+" Row: "+str(row)+" Col: "+str(col))
        arr[row][col] = str(value[int(x)])
        
        col = col + 1
        if col == column_count:
            col = 0
            row = row + 1
    
    
    #preparing result    
    res = ''
    
    #go for every row and parse data in defined in key order
    for data_row in arr:
        for order in key_arr:
            if str(data_row[int(order)-1]) != 'inf':
                res = res + str(data_row[int(order)-1])
            

    return res




res = encrypt_decrypt(sys.argv[1],sys.argv[2])

res2 = encrypt_decrypt(res,sys.argv[2])

print(res2)