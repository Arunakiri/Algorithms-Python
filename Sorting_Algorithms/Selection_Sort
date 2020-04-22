# Repeatedly finding minimum value from the array and
# Swap the minimum value to its appropriate position.

def Selection_Sort(arr):
	n = len(arr)
	
	for i in range(n-1):
		min_index = i
		
		for j in range(i+1, n):
			if arr[j] < arr[min_index]:
				min_index = j
		
		arr[i], arr[min_index] = arr[min_index], arr[i]
	
	return arr


# Driver Code
a = '9 8 7 6 5 4 3 2 1'
arr = list(map(int, a.split()))

Selection_Sort(arr)
