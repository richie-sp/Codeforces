n, d = [int(x) for x in input().split()]
info = []
for line in range(n):
    info.append([int(x) for x in input().split()])
info.sort()
 
l, r, ans, curr_fship, curr_d = 0, 0, info[0][1], info[0][1], 0
 
 
while l < len(info) and r < len(info):
    #increment r until difference is too much
    while True:
        r += 1
        if r == len(info):
            break
 
        curr_d = info[r][0] - info[l][0]
        curr_fship += info[r][1]
 
        if curr_d < d:
            ans = max(ans, curr_fship)
        if curr_d >= d:
            break
        
    
    #exit condition: 1. r == len(info)...here break 2. curr_d >= d ... then decrement till curr_d < d 
    if r == len(info):
        break
 
    while True:
        l += 1
 
        curr_fship -= info[l - 1][1]
 
        curr_d = info[r][0] - info[l][0]
 
        if curr_d < d:
            ans = max(ans, curr_fship)
            break
 
        if l == r: break
 
print(ans)