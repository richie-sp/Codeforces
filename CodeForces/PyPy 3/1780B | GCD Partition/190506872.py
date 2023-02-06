from sys import stdin
from math import ceil, gcd
input = stdin.readline
 
for case in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a); pre = 0; suf = total; ans = 1
    for i in range(len(a) - 1):
        pre += a[i]
        suf = total - pre
        ans = max(ans, gcd(pre, suf))
 
    print(ans)