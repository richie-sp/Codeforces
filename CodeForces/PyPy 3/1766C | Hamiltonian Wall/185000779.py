from sys import stdin
input = stdin.readline
 
for c in range(int(input())):
    m = int(input())
    grid = []
    for i in range(2):
        grid.append([ch for ch in input()[:-1]])
 
    ans = True
    for i in range(1, len(grid[0])):
        prev0, prev1, curr0, curr1 = grid[0][i - 1], grid[1][i - 1], grid[0][i], grid[1][i]
 
        if [prev0, prev1, curr0, curr1] == ['B', 'W', 'W', 'B'] or [prev0, prev1, curr0, curr1] == ['W', 'B', 'B', 'W']:
            ans = False; break
 
    if not ans:
        print('NO'); continue
 
    #classify the outs
    block_size = 0; out_by_col = [-1] * m
    for col in range(1, len(grid[0])):
        if not (grid[0][col] == 'B' and grid[1][col] =='B') and grid[0][col - 1] == 'B' and grid[1][col - 1] == 'B':
            if grid[0][col] == 'B':
                out = 0
            else:
                out = 1
            
            out_by_col[col - 1] = out
 
    #classify the INS
    block_size = 0; in_by_col = [-1] * m
    for col in range(1, len(grid[0])):
        if grid[0][col] == 'B' and grid[1][col] =='B' and not (grid[0][col - 1] == 'B' and grid[1][col - 1] == 'B'):
            if grid[0][col - 1] == 'B':
                ins = 0
            else:
                ins = 1
            
            in_by_col[col] = ins
 
 
    start_block = None; end_block = None; start_ends = []
    for col in range(len(grid[0])):
        if grid[0][col] == 'B' and grid[1][col] == 'B':
            if start_block is None:
                start_block = col; end_block = col
            end_block = col
        else:
            if start_block != None and end_block != None:
                start_ends.append((start_block, end_block))
            start_block = None; end_block = None
 
 
    for s, e in start_ends:
        block_size = e - s + 1
        start = in_by_col[s]; end = out_by_col[e]
 
        if block_size % 2 == 0:
            if start != -1 and end != -1:
                if start != end:
                    ans = False; break
        else:
            if start != -1 and end != -1:
                if start == end:
                    ans = False; break
    
    print('YES') if ans else print('NO')
 
 
            
 
            