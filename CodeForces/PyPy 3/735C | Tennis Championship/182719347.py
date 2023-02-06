import math
n = int(input())
n -= 1
 
fib = [1, 1]
while fib[-1] <= n:
    fib.append(fib[-1] + fib[-2])
 
s = 0; ans = 1
for i in range(len(fib)):
    s += fib[i]
    if s <= n:
        ans = i + 1
    else:
        break
 
print(ans)
 
 
 