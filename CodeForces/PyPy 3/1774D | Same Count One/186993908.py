from sys import stdin
input = stdin.readline 
 
for case in range(int(input())):
    n, m = map(int, input().split())
    a = []; inds_by_sum = [[] for k in range(m + 1)]; total_sum = 0; sum_by_row = [0 for i in range(n)]
    for line in range(n):
        row = list(map(int, input().split()))
        row_sum = sum(row); total_sum += row_sum
        sum_by_row[line] = row_sum
        inds_by_sum[row_sum].append(line)
        a.append(row)
 
    if total_sum % n != 0:
        print(-1); continue
 
    avg = total_sum // n
    
    if len(inds_by_sum[avg]) == n:
        print(0); continue
    
    l_inds = []; r_inds = []
    for row_sum, inds in enumerate(inds_by_sum):
        if row_sum < avg and inds:
            l_inds += inds
 
        if row_sum > avg and inds:
            r_inds += inds
 
 
    l_ptr = 0; r_ptr = 0; num_ops = 0; ops = []
    while l_ptr < len(l_inds) and r_ptr < len(r_inds):
        l_ind = l_inds[l_ptr]; r_ind = r_inds[r_ptr]
        l_sum = sum_by_row[l_ind]; r_sum = sum_by_row[r_ind]
        for i in range(m):
            # print('hi', l_ind, r_ind, l_sum, r_sum, i)
            if l_sum == avg or r_sum == avg: break
            if a[l_ind][i] == 0 and  a[r_ind][i] == 1:
                a[r_ind][i] = 0; a[l_ind][i] = 1
                r_sum -= 1; l_sum += 1; num_ops += 1; ops.append([str(l_ind + 1), str(r_ind + 1), str(i + 1)])
 
        sum_by_row[l_ind] = l_sum; sum_by_row[r_ind] = r_sum
 
        if l_sum == avg:
            l_ptr -= 1
 
        if r_sum == avg:
            r_ptr += 1
 
 
    print(num_ops)
    for o in ops:
        print(' '.join(o))