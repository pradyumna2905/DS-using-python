#!/usr/bin/python

n = input('Enter n: ')

arr=[]
arr=raw_input().split()
arr=[int(x) for x in arr]

max = arr[0]
min = max
for i in range(0, n):
	if arr[i] > max:
		max = arr[i]
	elif arr[i] < min:
		min = arr[i]

print 'MAX = %d, MIN = %d' %(max, min)
	















