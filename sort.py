#!/usr/bin/python

n = input('Enter n: ')

arr = []
print 'Enter values to sort'
arr = raw_input().split()
arr = [int(x) for x in arr]

print arr

for i in range(0, n+1):
	for j in range(i+1, n):
		if arr[i] > arr[j]:
			temp = arr[j]
			arr[j] = arr[i]
			arr[i] = temp
print arr




