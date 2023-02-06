from sys import stdin
input = stdin.readline
 
 
#Idea: Analyze the growth of 10 over time b/c this is the most fundamental string and every number turns into this eventually
#Precomputation
a = [1]; b = [1]; f = [2]; md = 10 ** 9 + 7
for k in range(1, 2 * 10 ** 5 + 1):
    if k - 10 >= 0:
        a.append(f[k - 10])
    else:
        a.append(a[-1])
 
    if k - 9 >= 0:
        b.append(f[k - 9])
    else:
        b.append(b[-1])
        
    f.append((a[-1] + b[-1]) % md)
 
for _ in range(int(input())):
    n, m = map(int, input().split())
 
    ans = 0
    for elem in str(n):
        ten_ops = 10 - int(elem)
        
        if m - ten_ops >= 0:
            ans += f[m - ten_ops]
        else:
            ans += 1
        ans %= md
 
    print(ans)