n, k, d = [int(x) for x in input().split()]
 
f = [[0 for j in range(n + 1)] for i in range(n + 1)]
g = [[0 for j in range(n + 1)] for i in range(n + 1)]
 
#f[x][y] = the number of paths length x with weight y
 
f[0][0], g[0][0] = 1, 1
 
f_count, g_count = 0, 0 
for x in range(n):
    for y in range(x, n):
        if f[x][y] == 0:
            break
 
        for diff in range(1, k + 1):
            try:
                f[x + 1][y + diff] += f[x][y]
                if y + diff == n: f_count += (f[x][y])
            except:
                break
 
        for diff in range(1, d):
            try:
                g[x + 1][y + diff] += g[x][y]
                if y + diff == n: g_count += (g[x][y])
            except:
                break
 
print((f_count - g_count) % (10 ** 9 + 7))
 
 
 
 
 
 
 
    