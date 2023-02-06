n = int(input())
 
 
mod = 10 ** 9 + 7
d, a = 1, 0
for i in range(1, n + 1):
    prev_d = d
    d = (3 * a) % mod
    a = (prev_d + 2 * a) % mod
 
 
print(d)