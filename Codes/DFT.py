# ---- A Drunk Man Will Find His Way Home but a Drunk Bird May Get Lost Forever =) ---- 
# Discrete Fourier transform in python. 
import math 

# defining CIS (cos(x) + j sin(x)) function 
def cis(x):
    a = math.cos(x)
    b = math.sin(x)
    c = complex(a , b)
    return c 

# we have to make a function to make cis(2*k*pi / n) for fourier transform , i'll call it "Ws" 
def Ws(k,n):
    return cis((2*k*math.pi)/n)


# now all we have to do is to make them work 
n = int(input("please enter size of your array \n"))
arr_input = []
arr_ans = [0] * n
arr_Ws = []

for i in range(0,n):
    temp = complex(input())
    arr_input.append(temp)
    #lets create our Ws in here to
    arr_Ws.append(Ws(i,n)) 

#making the DFT Work.
for i in range(0,n):
    for j in range(0,n):
        arr_temp =[0] * n
        arr_temp[j] =  arr_input[j] * (arr_Ws[i])**j
    arr_ans[i] = sum(arr_temp)

print(arr_ans)
