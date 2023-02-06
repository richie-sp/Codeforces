n, m, k = map(int, input().split())
grid = []
top_row, bottom_row = None, None
for l in range(n):
    row = [e for e in input()]
    grid.append(row)
 
visited = set(); islands = []; lengths = []
for i in range(n):
    for j in range(m):
        if (i, j) in visited or grid[i][j] == '*': continue
        ocean = False
        island = set([(i, j)])
        dfs = [(i, j)]
        while dfs:
            x1, y1 = dfs.pop()
            if x1 in [0, n - 1] or y1 in [0, m - 1]: ocean = True
            adjacents = [(x2, y2) for x2, y2 in [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)] if 0 <= x2 < n and 0 <= y2 < m and (x2, y2) not in island and (x2, y2) not in visited and grid[x2][y2] == '.']
            for x2, y2 in adjacents:
                island.add((x2, y2))
                dfs.append((x2, y2))
 
        for x, y in island: visited.add((x, y))
        if not ocean: islands.append(island)
 
islands = sorted(islands, key = lambda x: len(x))
 
ans = 0
for i in range(len(islands) - k):
    for x, y in islands[i]:
        ans += 1
        grid[x][y] = '*'
 
print(ans)
for row in grid:
    print(''.join(row))
        
 