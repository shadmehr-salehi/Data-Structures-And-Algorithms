#Honer Algorhitm implementation
# ---- A Drunk Man Will Find His Way Home but a Drunk Bird May Get Lost Forever =) ----

# 2 X^3 + 3 X^2 -4X + 1 = 1185
CoeArr = [] 
n = int(input("please enter number of Coeffisents \n"))
for i in range(n):
    Coe = int(input("please enter Coe {} \n".format(i)))
    CoeArr.append(Coe)

sum = CoeArr[0]
x = int(input("please enter number X \n"))

for i in range(1,n):
    sum = x*sum + CoeArr[i]

print(sum)
