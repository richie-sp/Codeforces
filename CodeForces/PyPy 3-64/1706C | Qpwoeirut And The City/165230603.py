import math
for case in range(int(input())):
    n = int(input())
    h = [int(h_i) for h_i in input().split()]
    max_cool = int(math.ceil((n-2)/2))
    
    if n % 2 == 1:
        #avoid start and last indices
        additional = 0
        for i in range(1, n-1, 2):
            additional += max(0, max(h[i+1], h[i-1]) - h[i] + 1)
 
        print(additional)
        continue
 
    r = [0 for i in range(n)]
    l = [0 for i in range(n)]
 
    for i in range(1, n-2, 2):
        if i == 1:
            l[i] = max(0, max(h[i+1], h[i-1]) - h[i] + 1)
        else:
            l[i] = l[i-2] + max(0, max(h[i+1], h[i-1]) - h[i] + 1)
 
    for i in range(n-2, 1, -2):
        if i == n-2:
            r[i] = max(0, max(h[i+1], h[i-1]) - h[i] + 1)
        else:
            r[i] = r[i+2] + max(0, max(h[i+1], h[i-1]) - h[i] + 1)
 
    min_aug = float('inf')
    min_aug = min(min_aug, l[n-3], r[2])
    for i in range(1, n - 4, 2):
        min_aug = min(min_aug, l[i] + r[i + 3])
 
    
    print(min_aug)
 
 
            
 
 
 
 
    