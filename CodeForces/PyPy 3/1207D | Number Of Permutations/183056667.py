from sys import stdin
from collections import Counter
input = stdin.readline
 
pair_ctr = Counter(); first_ctr = Counter(); second_ctr = Counter()
 
s = []; prime = 998244353; n = int(input()); factorial = [1, 1]
 
for i in range(2, n  + 1):
    factorial.append((factorial[-1] * i) % prime)
 
ans = factorial[n]
 
for l in range(n):
    a, b = map(int, input().split())
    pair_ctr[(a, b)] += 1; first_ctr[a] += 1; second_ctr[b] += 1; s.append((a, b))
    
#bad1, bad2, bad12
bad12 = 1; bad1 = 1; bad2 = 1; mult = 1
 
 
s.sort()
prev_a, prev_b = float('-inf'), float('-inf')
for a, b in s:
    if a < prev_a or b < prev_b:
        mult = 0; break
    prev_a = a; prev_b = b
 
if mult == 1:
    for v in pair_ctr.values(): 
        bad12 *= factorial[v]
        bad12 %= prime
else:
    bad12 = 0
 
for v in first_ctr.values():
    bad1 *= factorial[v]
    bad1 %= prime
 
for v in second_ctr.values():
    bad2 *= factorial[v]
    bad2 %= prime
 
ans -= (bad1 + bad2 - bad12)
ans %= prime
 
print(ans)
 
 
 
 
 
    