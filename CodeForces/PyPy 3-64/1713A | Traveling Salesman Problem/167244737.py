for case in range(int(input())):
    n = int(input())
    
    min_x = float('inf')
    min_y = float('inf')
    max_x = float('-inf')
    max_y = float('-inf')
    for line in range(n):
        x, y = [int(a) for a in input().split()]
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    
    ans = 0
    
    if min_x < 0 and max_x < 0:
        ans += 2 * abs(min_x)
    elif min_x < 0 and max_x >= 0:
        ans += 2 * abs(min_x)
        ans += 2 * max_x
    elif min_x >= 0 and max_x >= 0:
        ans += 2 * max_x
 
    if min_y < 0 and max_y < 0:
        ans += 2 * abs(min_y)
    elif min_y < 0 and max_y >= 0:
        ans += 2 * abs(min_y)
        ans += 2 * max_y
    elif min_y >= 0 and max_y >= 0:
        ans += 2 * max_y
 
    print(ans)
 