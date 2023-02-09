#Shell Sort implementation
# ---- A Drunk Man Will Find His Way Home but a Drunk Bird May Get Lost Forever =) ----

def shellSort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap  = gap//2
 
 
# Driver code to test above
arr = [ 12, 34, 54, 2, 3]
n = len(arr) 
shellSort(arr)
 
print ("\nArray after sorting:")
for i in range(n):
    print(arr[i])
 
