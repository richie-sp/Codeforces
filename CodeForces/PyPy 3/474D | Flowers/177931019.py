from itertools import accumulate
 
t, k = [int(x) for x in input().split()]
 
f, w, r = [0] * (100001), [0] * (100001), [0] * (100001)
f[0] = 1
mod = 10 ** 9 + 7
for i in range(1, 100001):
    r[i] = f[i - 1]
    if i - k >= 0: 
        w[i] = f[i - k]
    f[i] = (w[i] + r[i]) % mod
 
p_sum = list(accumulate(f))
 
for case in range(t):
    a, b = [int(x) for x in input().split()]
    print((p_sum[b] - p_sum[a - 1]) % mod)
 
    