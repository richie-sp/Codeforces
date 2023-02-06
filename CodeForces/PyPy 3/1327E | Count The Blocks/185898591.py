from sys import stdin
input = stdin.readline
 
def inv(a, n):
    if(a == 1):
        return 1
    return int((1 - inv(n % a, a) * n) / a + n)
 
n = int(input()); ans = []; ten_power = [1]; prime = 998244353; inverses = [inv(1, prime)]
for i in range(1, n + 1):
    ten_power.append((ten_power[-1] * 10) % prime)
    inverses.append(inv(ten_power[-1], prime))
blocks = ten_power[n]
 
ans = []
for b in range(1, n + 1):
    if b == n:
        ans.append(10)
    else:
        ans.append((blocks * ((2 * 10 * inverses[b] * 9 * inverses[1]) + max(0, n - b - 1) * 10 * inverses[b] * 9 ** 2 * inverses[1] ** 2)) % prime)
 
print(' '.join((str(e) for e in ans)))
 
    
 
        
 
        
 