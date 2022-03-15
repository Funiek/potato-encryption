#!/usr/bin/python3
def encrypt(value:str,key:str):
	a=[0]*len(value)
	zwrot = -1
	for i,v in enumerate(value):
		if i == 0:
			a[i] = 1
			continue
		if zwrot == -1:
			a[i] = a[i-1]+1
		else:
			a[i] = a[i-1]-1
		if a[i] == int(key) or a[i] == 1:
			zwrot = (-1) * zwrot
	
	ret = []
	for ii in range(1,int(key)+1):
		for i,v in enumerate(value):
			if a[i] == ii:
				ret.append(v)
	return ''.join(ret)
import sys
print(encrypt(sys.argv[1],sys.argv[2]))
