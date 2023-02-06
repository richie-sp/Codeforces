"""
Accepted
"""
from sys import stdin
import bisect
input = stdin.readline
 
k, q = map(int, input().split()); eps = 10 ** (-7)
p_max = 0.5
f = [[0.0 for i in range(k + 1)], [0.0 for i in range(k + 1)]]; f[0][0] = 1.0; f[1][1] = 1.0
for i in range(2, 10 ** 5):
    arr = [0.0 for i in range(k + 1)]
    for j in range(1, k + 1):
        arr[j] = f[-1][j] * j / k + f[-1][j - 1] * (k - j + 1) / k
    f.append(arr)
    if arr[k] >= p_max:
        break
 
L = [f[i][-1] for i in range(len(f))]
 
for _ in range(q):
    p = int(input());
    print(bisect.bisect_right(L, p/2000))
 
    
    