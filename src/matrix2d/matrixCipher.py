#!/usr/bin/python3

def encrypt(message:str,key:str):
	k_array = getArrayKey(key)
	message = message.replace(" ",'')
	n = len(k_array)
	m = (len(message)*2-1)//n
	#print(f"n={n}  message={message} k_array={k_array}")

	ret = []

	for y in k_array:
		index = 1
		while index+y-2 < len(message):
			ret.append(message[index+y-2])
			index += len(k_array)
		ret.append(" ")
	return ''.join(ret[:-1])
		

def getArrayKey(key:str):
	arr = list(range(1,int(len(key))+1))
	arr = list(zip(key,arr))
	arr.sort()
	#print(arr)
	arr = [i[1] for i in arr]
	return arr
import sys
print(encrypt(sys.argv[1],sys.argv[2]))

	
