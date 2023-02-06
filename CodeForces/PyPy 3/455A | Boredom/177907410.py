from collections import Counter
 
n = int(input())
 
arr = [int(x) for x in input().split()]
 
ct = Counter(arr)
 
max_val, min_val = max(ct), min(ct)
 
f = [0 for i in range(max_val + 1)]
 
 
for i in range(min_val, max_val + 1):
    f[i] = max(f[i], ct[i] * i)
    if i >= 1:
        f[i] = max(f[i], f[i - 1], f[i])
 
    if i >= 2:
        f[i] = max(ct[i] * i + f[i - 2], f[i])
 
 
print(f[max_val])
 
 
 