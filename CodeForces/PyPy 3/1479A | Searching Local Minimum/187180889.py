from sys import stdin, stdout
input = stdin.readline
 
n = int(input()); l = 1; r = n
 
lrs = []; previously_queried = [None for i in range(n + 1)]
while l < r - 1:
    m = (l + r) // 2; lrs.append((l, r))
    if previously_queried[m] is None:
        print(f'? {m}'); stdout.flush(); a_m = int(input()); previously_queried[m] = a_m
    else: a_m = previously_queried[m]
    if previously_queried[l] is None:
        print(f'? {l}'); stdout.flush(); a_l = int(input()); previously_queried[l] = a_l
    else: a_l = previously_queried[l]
    if a_l < a_m:
        l, r = l, m - 1; continue 
 
    if previously_queried[r] is None:
        print(f'? {r}'); stdout.flush(); a_r = int(input()); previously_queried[r] = a_r
    else: a_r = previously_queried[r]
    if a_r < a_m:
        l, r = m + 1, r; continue 
 
    #now a_l > a_m and a_r > a_m
    m1 = (l + m) // 2; m2 = (m + r) // 2
    if previously_queried[m1] is None:
        print(f'? {m1}'); stdout.flush(); a_m1 = int(input()); previously_queried[m1] = a_m1
    else: a_m1 = previously_queried[m1]
    if a_m1 < a_m and a_m1 < a_l:
        l, r = l + 1, m - 1; continue
 
    if previously_queried[m2] is None:
        print(f'? {m2}'); stdout.flush(); a_m2 = int(input()); previously_queried[m2] = a_m2
    else: a_m2 = previously_queried[m2]
 
    if a_m2 < a_m and a_m2 < a_r:
        l, r = m + 1, r - 1; continue
 
    l, r = m1 + 1, m2 - 1
 
lrs.append((l, r))
 
if previously_queried[l] is None:
        print(f'? {l}'); stdout.flush(); a_l = int(input()); previously_queried[l] = a_l
else: a_l = previously_queried[l]
 
if previously_queried[r] is None:
        print(f'? {r}'); stdout.flush(); a_r = int(input()); previously_queried[r] = a_r
else: a_r = previously_queried[r]
 
if a_l < a_r:
    print(f'! {l}')
else:
    print(f'! {r}')
 
 