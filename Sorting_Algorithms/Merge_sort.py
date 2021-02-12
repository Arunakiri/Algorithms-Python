# Merge Sort algorithm is a Divide and Conquer algorithm.
# We use two functions; one for dividing part and one for the conquering(merging) part 
# merge_sort(): - dividing the array using recursion. Follow the branches of the recursion tree.
# merge(): - merging the divided arrays in sorted order. 
# Note: Since there will always be one or many elements in one of those two arrays has the biggest element, it will be left out.
#       Add that element seperately.


def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    
    return result

def Merge_Sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)
  
  
# Driver Code  
a = '38 27 43 3 9 82 10'
arr = list(map(int, a.split()))

Merge_Sort(arr)
