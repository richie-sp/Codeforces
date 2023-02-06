import math
 
n, m = [int(x) for x in input().split()]
 
maxim  = math.comb(n - m + 1, 2)
 
if n % m == 0:
    minim = m * math.comb(n // m, 2)
else:
    s = n // m
    l = s + 1
 
    r_l = n / m - n // m
    r_s = 1 - r_l 
 
    n_s, n_l = round(r_s * m), round(r_l * m)
 
    minim = n_s * math.comb(s, 2) + n_l * math.comb(l, 2)
 
 
 
print(minim, maxim)