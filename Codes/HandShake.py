#There are Even Amount of people standing around a table , they want to shake hands but 2 hands should never cross each other 
# this code calculates the number of solutions 

dp = [1,0,1]
n = int(input())
for i in range(3,n+1):
    dp.append(0)
    for j in range(0,i-1):
        dp[i] = dp[i] + dp[j] * dp[i-j-2]
print(dp[n]) 

# time complexity =O(n^2)
