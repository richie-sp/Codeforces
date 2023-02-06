def gen_bad_points(sx: int, sy: int, d: int) -> set:
    #these points are in a diamond shape
    pass
 
 
for case in range(int(input())):
    n, m, sx, sy, d = [int(x) for x in input().split()]
    #make 0 indexed
    sx, sy = sx-1, sy-1
 
    x = abs(0 - sx) > d
    w = abs((n-1) - sx) > d
    z = abs(0 - sy) > d
    y = abs((m-1) - sy) > d
 
    print(n + m - 2) if (x and y) or (z and w) else print(-1)