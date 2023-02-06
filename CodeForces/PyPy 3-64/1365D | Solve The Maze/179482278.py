from sys import stdin
from collections import deque
input = stdin.readline
# import datetime
 
for case in range(int(input())):
    n, m = map(int, input().split())
 
    grid = []
    for l in range(n):
        grid.append([ch for ch in input()[:-1]])
 
 
    cross_g = False; g_inds = []
    for i in range(n):
        if cross_g: break
        for j in range(m):
            if grid[i][j] == 'B':
                adjacents = [(u, v) for u, v in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)] if 0 <= u < n and 0 <= v < m]
                for u, v in adjacents:
                    if grid[u][v] == 'G':
                        cross_g = True
                    if grid[u][v] == '.': grid[u][v] = '#'
 
            if grid[i][j] == 'G': g_inds.append((i, j))
 
            if cross_g: break
    
    if cross_g: print('nO'); continue
    # t1 = datetime.datetime.now()
    ans = True; g_inds = set(g_inds); verified = set()
    for loc in g_inds:
        if loc in verified: continue
        bfs = deque([loc])
        visited = set([loc])
        path = False
        curr_g_inds = []
        while bfs:
            i, j = bfs.popleft()
            if (i, j) in g_inds: curr_g_inds.append((i, j))
            if (i, j) == (n - 1, m - 1):
                path = True
                break
 
            adjacents = [(u, v) for u, v in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)] if 0 <= u < n and 0 <= v < m and grid[u][v] != '#' and (u, v) not in visited]
            for u, v in adjacents:
                visited.add((u, v))
                bfs.append((u, v))
 
        if not path:
            ans = False
            break
 
        for good_loc in curr_g_inds: verified.add(good_loc)
    
    # t2 = datetime.datetime.now()
    # print(t2 - t1)
    print('yEs') if ans else print('nO')
 