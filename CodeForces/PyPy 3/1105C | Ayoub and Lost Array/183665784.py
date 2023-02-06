n, l, r = [int(x) for x in input().split()]
 
l_min = l - 6; l_min -= (l_min % 3); r_max = r + 6; r_max -= (r_max % 3); ct = [0] * 3; ct[0] = (r_max - l_min) // 3 + 1; ct[1] = ct[0] - 1; ct[2] = ct[0] - 1
 
 
for i in range(l_min, l):
    ct[i % 3] -= 1
 
for i in range(r_max, r, -1):
    ct[i % 3] -= 1
 
f = [[0 for j in range(3)] for i in range(n + 1)]; f[1][0], f[1][1], f[1][2] = ct[0], ct[1], ct[2]; m = 10 ** 9 + 7
 
for i in range(2, n + 1):
    f[i][0] = (ct[0] * f[i - 1][0] + ct[1] * f[i - 1][2] + ct[2] * f[i - 1][1]) % m
    f[i][1] = (ct[0] * f[i - 1][1] + ct[1] * f[i - 1][0] + ct[2] * f[i - 1][2]) % m
    f[i][2] = (ct[0] * f[i - 1][2] + ct[1] * f[i - 1][1] + ct[2] * f[i - 1][0]) % m
 
print(f[n][0])
 