a = input()
b = input()
grid = [[1 if ch == 'X' else 0 for ch in a], [1 if ch == 'X' else 0 for ch in b]]
 
ans = 0
 
for i in range(1, len(a)):
    p2, p1 = grid[0][i], grid[0][i - 1]
    p4, p3 = grid[1][i], grid[1][i - 1]
    sq_ct = [p1, p2, p3, p4].count(0)
    if sq_ct < 3:
        continue
    elif sq_ct == 3:
        grid[0][i] = 1; grid[0][i - 1] = 1; grid[1][i] = 1; grid[1][i - 1] = 1; ans += 1
    else:
        if i == len(a) - 1:
            ans += 1
        else:
            p5 = grid[0][i + 1]; p6 = grid[1][i + 1]
            if p5 == 0 and p6 == 0:
                grid[0][i] = 1; grid[0][i - 1] = 1; grid[1][i] = 1; grid[1][i - 1] = 1; grid[0][i + 1] = 1; grid[1][i + 1] = 1; ans += 2
            else:
                grid[0][i] = 1; grid[0][i - 1] = 1; grid[1][i] = 1; grid[1][i - 1] = 1; ans += 1
 
 
print(ans)
 
                
        
    