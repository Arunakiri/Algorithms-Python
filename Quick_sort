# Choose a random Pivot point.
# Seperating the lower, higher and equal parts.
# Use Recursion to repeat the process.


from random import randint 

def Quick_Sort(arr):
    n = len(arr)
    
    if n <= 1:
        return arr
    
    smaller, equal, larger = [], [], []
    
    pivot = arr[randint(0, n-1)]
    
    for each in arr:
        if each < pivot:    smaller.append(each)
        elif each == pivot: equal.append(each)
        else:               larger.append(each)
        
    return Quick_Sort(smaller) + equal + Quick_Sort(larger)
    

# Driver Code
a = '9 8 7 6 5 4 3 2 1'
arr = list(map(int, a.split()))

Quick_Sort(arr)
