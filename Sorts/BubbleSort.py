#Bubble Sort implementation
def bubblesort(elements):
   for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]   



a = [1,2,3,10,23,0]

bubblesort(a)
print(a)


