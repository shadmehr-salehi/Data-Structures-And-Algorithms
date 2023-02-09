# we want to remove same substrings in a list of chars
# EG : abbaca : abbaca -> aaca -> ca  

# ---- A Drunk Man Will Find His Way Home but a Drunk Bird May Get Lost Forever =) ----

def check(s:list):
    for i in range(1,len(s)):
        if(s[i-1] == s[i]):
            return True
    return False


list = list(input())
while check(list):
    for i in range(1,len(list)+1):
        if(list[i] == list[i-1]):
            list.pop(i)
            list.pop(i-1)
            break
list = "".join(list)
print(list)

