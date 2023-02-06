from sys import stdin
input = stdin.readline
 
 
def inv(a, n):
    if(a == 1):
        return 1
    return int((1 - inv(n % a, a) * n) / a + n)
 
m = 998244353
n = int(input())
p = list(map(int, input().split()))
q = [((100 - elem) * inv(100, m)) % m for elem in p]
p = [(elem * inv(100, m)) % m for elem in p]
 
k = 0; a = 1; b = 0
while True:
    a = ((a - q[k]) * inv(p[k], m)) % m; b = ((b - 1) * inv(p[k], m)) % m
    k += 1
    
    if k == n:
        break
 
print((-b * inv(a, m)) % m)
    
 
 
 
 
 