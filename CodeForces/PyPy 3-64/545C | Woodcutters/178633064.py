tree_info = []
 
for line in range(int(input())):
    tree_info.append([int(x) for x in input().split()])
 
ans = 0
prev_max = None
for i, info in enumerate(tree_info):
    x, h = info
    if i == 0:
        ans += 1
        prev_max = tree_info[0][0]
        continue
     
    l_pos, r_pos = x - h, x + h
 
    #see if l_pos is valid
    if l_pos > prev_max:
        ans += 1
        prev_max = x
        continue
 
    #see if r_pos is valid
    if i == len(tree_info) - 1:
        ans += 1
    else:
        if r_pos < tree_info[i + 1][0]:
            ans += 1
            prev_max = r_pos
        else:
            prev_max = x
    
 
print(ans)
 
 