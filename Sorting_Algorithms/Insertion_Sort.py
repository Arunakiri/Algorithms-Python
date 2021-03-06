# Just like Playing Cards.
# Choose an element and swap all the elements before if they are higher.


def Insertion_Sort(arr):
	n = len(arr)
	
	for i in range(1, n):
		
		k = arr[i]
		
		j = i-1
		
		while j >= 0 and arr[j] > k:
			arr[j+1] = arr[j]
			j -= 1
		
		arr[j+1] = k
	
	return arr


# Driver Code
a = '9 8 7 6 5 4 3 2 1'
arr = list(map(int, a.split()))

Insertion_sort(arr)
