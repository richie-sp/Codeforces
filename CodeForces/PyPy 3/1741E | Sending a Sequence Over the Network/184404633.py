from sys import stdin
input = stdin.readline 
 
for c in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
 
    #f[0] refers for empty string which is vacuously true
    f = [False for i in range(n + 1)]; f[0] = True 
 
    for i in range(1, n + 1):
        if i + b[i - 1] <= n and f[i - 1]: f[i + b[i - 1]] = True
        if i - b[i - 1] - 1 >= 0 and f[i - b[i - 1] - 1]: f[i] = True
 
    print('yEs') if f[n] else print('nO')