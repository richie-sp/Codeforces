for case in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
 
    f, g = [0] * (n + 1), [0] * (n + 1) 
 
    f[n - 1] = a[n - 1]
 
    for i in range(n - 2, -1, -1):
        f[i] = min(a[i] + g[i + 1], a[i] + a[i + 1] + g[i + 2])
        g[i] = min(f[i + 1], f[i + 2])
 
    print(f[0])