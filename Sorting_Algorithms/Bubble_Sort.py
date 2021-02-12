# Comparing Adjacent elements and Swapping them.
# Repeat the loop untill sorted.
# Note: No. of loops is equal to the length of the array

def Bubble_Sort(arr):
	n = len(arr)
	
	for i in range(n):
		for j in range(n-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	
	return arr
	
# Driver Code
a = '9 8 7 6 5 4 3 2 1'
arr = list(map(int, a.split()))

Bubble_Sort(arr)
