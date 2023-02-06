from sys import stdin
input = stdin.readline
 
 
dp = [False for i in range(1101)]
dp[0] = True
for i in range(len(dp)):
    if i - 11 >= 0 and dp[i - 11]:
        dp[i] = True
        continue
 
 
    if i - 111 >= 0 and dp[i - 111]:
        dp[i] = True
        continue
    
 
for c in range(int(input())):
    x = int(input())
    if x >= 1100:
        print('yEs')
        continue
    else:
        print('YeS') if dp[x] else print('nO')