from sys import stdin
input = stdin.readline
 
for case in range(int(input())):
    n, m, d = map(int, input().split())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ind_by_val = [None for i in range(n + 1)]
    for ind, val in enumerate(p):
        ind_by_val[val] = ind + 1
 
    ans = float('inf')
    for i in range(1, len(a)):
        prev = a[i - 1]; curr = a[i]
        prev_pos = ind_by_val[prev]; curr_pos = ind_by_val[curr]
        if prev_pos > curr_pos or prev_pos + d < curr_pos:
            ans = 0; break
 
        """
        try to increment curr_pos
        """
        #move to right
        if prev_pos + d + 1 <= n:
            ans = min(ans, prev_pos + d + 1 - curr_pos)
        #move to left
        if curr_pos - d - 1 >= 1:
            ans = min(ans, prev_pos - (curr_pos - d - 1))
 
        #swap
        ans = min(ans, abs(curr_pos - prev_pos))
 
        #move to left and to the right
        if 1 + d + 1 <= n:
            ans = min(ans, d + 1 - (curr_pos - prev_pos))
 
        
 
    print(ans)