# ---- A Drunk Man Will Find His Way Home but a Drunk Bird May Get Lost Forever =) ----
def isoperator(x):
    return (x == '*' or x == '/' or x == '+' or x == '-' or x == '^' or x == '%')

def getinfix(exp):
    stack = []
    for i in exp:
        if isoperator(i):
            temp = stack[0]
            stack.pop(0)
            stack.insert(0,i)
            stack.insert(0,temp)
        else:
            stack.insert(0,i)
    
    # for i in range(len(exp)):
    #     exp[i] = stack[0]
    #     stack.pop(0)
    stack.reverse()
    ans = "".join(stack)
    print(ans)


if __name__ =="__main__":
    exp = input()
    exp = list(exp)
    getinfix(exp)
