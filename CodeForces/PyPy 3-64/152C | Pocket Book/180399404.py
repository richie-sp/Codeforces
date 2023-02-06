from sys import stdin
input = stdin.readline
from collections import defaultdict
 
n, m = map(int, input().split())
chars_by_ind = defaultdict(set)
for l in range(n):
    s = input()
    for ind, ch in enumerate(s): chars_by_ind[ind].add(ch)
 
ans = 1; mod = 10 ** 9 + 7
for ind in range(m):
    ans *= len(chars_by_ind[ind])
    if ans > mod: ans %= mod
 
print(ans)