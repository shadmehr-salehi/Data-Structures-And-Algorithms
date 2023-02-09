#queue in python using list
n = int(input())
q = [0] * n 
l = 0
for i in range(n):
    RawString = str(input())
    if(len(RawString) > 4):
        string = list(RawString.split(" "))
        num = int(string[1])
        q[l] = num
        l = l+1
    elif(len(RawString) == 3):
        print(q[0])
        q = q[1:n]
        l = l-1    
 
