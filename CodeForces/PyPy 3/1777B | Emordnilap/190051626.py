from sys import stdin
input = stdin.readline
 
fac = [1 for i in range(100001)]; mod = 10 ** 9 + 7
for i in range(1, 100000 + 1):
    fac[i] = (i * fac[i - 1]) % mod
 
for case in range(1, int(input()) + 1):
    n = int(input())
    print((fac[n] * n * (n - 1)) % mod)