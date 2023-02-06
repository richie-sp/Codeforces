from sys import stdin
input = stdin.readline
 
for c in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    max_val = max(a); min_val = min(a)
 
    if max_val == min_val:
        print(n * (n - 1)); continue 
        
    maxim = float('-inf'); minim = float('inf'); max_ct = 0; min_ct = 0
 
    for elem in a:
        if elem > maxim:
            maxim = elem; max_ct = 1
        elif elem == maxim:
            max_ct += 1
 
        if elem < minim:
            minim = elem; min_ct = 1
        elif elem == minim:
            min_ct += 1
 
    
 
    print(2 * max_ct * min_ct)