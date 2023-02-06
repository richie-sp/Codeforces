from sys import stdin
from collections import defaultdict, Counter
import itertools
input = stdin.readline 
 
for c in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if len(a) <= 2:
        print(0); continue
 
    differences = set()
    for i in range(n):
        for j in range(i + 1, n):
            differences.add((a[j] - a[i]) / (j - i))
 
 
    differences_by_ind = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i == j: continue
            differences_by_ind[i].append((a[j] - a[i]) / (j - i))
 
    ans = float('inf')
    for ind in differences_by_ind:
        ctr = Counter(differences_by_ind[ind])
        ans = min(ans, len(differences_by_ind[ind]) - ctr.most_common(1)[0][1])
 
 
    print(ans)