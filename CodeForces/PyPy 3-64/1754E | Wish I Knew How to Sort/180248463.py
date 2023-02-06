from sys import stdin
from math import comb
input = stdin.readline
 
 
def inv(a, n):
    if(a == 1):
        return 1
    return int((1 - inv(n % a, a) * n) / a + n)
 
 
for case in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    num_ones = sum(a)
    incorrect_inds = num_ones - sum(a[-num_ones:])
    mod = 998244353
    ans = 0
    total_pairs = comb(n, 2)
    for i in range(incorrect_inds, 0, -1):
        ans += (total_pairs * inv(i ** 2, mod))
        ans %= mod
 
    if ans == 0:
        print(0)
        continue
 
    p, q = ans.as_integer_ratio()
    
    print((p * inv(q, mod)) % mod)