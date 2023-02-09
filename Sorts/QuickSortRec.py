#Recursive QuickSort implementation
# ---- A Drunk Man Will Find His Way Home but a Drunk Bird May Get Lost Forever =) ----
def quicksort_recursive(a):
    if len(a) == 0:
        return a
    p = len(a) // 2
    l = [i for i in a if i < a[p]]
    m = [i for i in a if i == a[p]] 
    r = [i for i in a if i > a[p]]
    return quicksort_recursive(l) + m + quicksort_recursive(r)






l = [2,3,4,5,6,1,100,299,123]
print(quicksort_recursive(l))

