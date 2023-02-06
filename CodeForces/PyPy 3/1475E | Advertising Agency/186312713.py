from sys import stdin
from collections import Counter
input = stdin.readline
 
def inv(a, n):
    if(a == 1):
        return 1
    return int((1 - inv(n % a, a) * n) / a + n)
 
prime = 10 ** 9 + 7
factorial = [1, 1]
for i in range(2, 1001):
    factorial.append(factorial[-1] * i % prime)
 
 
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
 
    a.sort(); maxim_ctr = Counter(a[:-k]); a_ctr = Counter(a); ans = 1
    for val, r in maxim_ctr.items():
        m = a_ctr[val]
        ans *= (factorial[m] * inv(factorial[r], prime) * inv(factorial[m - r], prime))
        ans %= prime
 
    print(ans)
 
 
 
    