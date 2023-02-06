from sys import stdin
from collections import deque
input = stdin.readline 
 
n, m, k = map(int, input().split())
 
grid = []
for line in range(n):
    grid.append([ch for ch in input()[:-1]])
 
empty = 0; loc = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '.': 
            empty += 1; loc = (i, j)
 
 
bfs = deque([loc]); marked = 0; visited = set()
while bfs:
    i, j = bfs.popleft(); marked += 1; grid[i][j] = 'C'
    if marked == empty - k: break
    adjacents = [(u, v) for u, v in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)] if 0 <= u < len(grid) and 0 <= v < len(grid[0]) and (u, v) not in visited and grid[u][v] == '.']
    for nex_loc in adjacents:
        visited.add(nex_loc); bfs.append(nex_loc)
 
 
ans = [['.' for j in range(len(grid[0]))] for i in range(len(grid))]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#': ans[i][j] = '#'
        if grid[i][j] == 'C': ans[i][j] = '.'
        if grid[i][j] == '.': ans[i][j] = 'X'
 
for row in ans:
    print(''.join(row))