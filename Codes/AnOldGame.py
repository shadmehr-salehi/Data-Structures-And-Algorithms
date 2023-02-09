n,k = input().split(" ")
n = int(n)
k = int(k)


s = []
for i in range(1,n+1):
    s.append(i)


while len(s) > 1:
    l = len(s)
    flag = 0
    if(k%l == 0):
        flag = 1
    temp = s[0:k%l-1]
    if len(s) < k:
        s.pop(k%l-1)


    else:
        s.pop(k%l-1)


    s = s+temp
    s = s[k%l-1:len(s)]
    if(flag):
        s = temp


print(s[0])
