#!/usr/bin/python

def asc_sort(small_arr):
	for i in range(0, len(small_arr)):
		for j in range(i+1, len(small_arr)+1):
			if arr[i] < arr[j]:
				temp = arr[j]
				arr[j] = arr[i]
				arr[i] = temp

	return small_arr

def dec_sort(large_arr):
	for i in range(0, len(large_arr)):
		for j in range(i+1, len(large_arr)+1):
			if arr[i] > arr[j]:
				temp = arr[j]
				arr[j] = arr[i]
				arr[i] = temp

	return large_arr

n = input('Enter n: ')

arr=[]
large=[]
small=[]
arr=raw_input().split()
arr=[int(x) for x in arr]

print arr

for i in range(0,n):
	for j in range(i+1, n):
		if arr[i] > arr[j]:
			large.append(arr[i])
			small.append(arr[j])
		else:
			large.append(arr[j])
			small.append(arr[i])

print large
print small

min_arr=asc_sort(small)
max_arr=dec_sort(large)

print 'MAX = %d, MIN=%d' %(max_arr[-1], min_arr[0])













