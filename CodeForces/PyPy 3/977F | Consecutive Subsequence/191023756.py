from sys import stdin
from collections import defaultdict
input = stdin.readline
 
n = int(input())
a = list(map(int, input().split()))
 
longest_by_val = defaultdict(int)
 
ans = 1; best_ind = n - 1
 
for i in range(len(a) - 1, -1, -1):
    curr = longest_by_val[a[i] + 1] + 1
    if curr > ans:
        ans = curr; best_ind = i
    longest_by_val[a[i]] = max(longest_by_val[a[i]], curr)
 
best_val = a[best_ind]; seq = [str(best_ind + 1)]; curr = best_val + 1
for i in range(best_ind + 1, n):
    ind = i; elem = a[i]
    if curr == best_val + ans: break
    if elem == curr:
        curr += 1; seq.append(str(ind + 1))
 
 
print(ans)
print(' '.join(seq))
 
 
 
 
 
 
 