from collections import defaultdict
t = int(input())
 
for case in range(t):
    n = int(input())
    a = [int(x) for x in input()]
 
    prefix_sum = [0 for elem in a]
    prefix_sum[0] = a[0]
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = prefix_sum[i-1] + a[i]
    prefix_sum = [0] + prefix_sum
 
    adj_ps_by_ind = defaultdict(set)
 
    for i, s in enumerate(prefix_sum):
        adj_ps_by_ind[s - i].add(i)
 
    # print(prefix_sum)
 
    # print(adj_ps_by_ind)
 
    ans = 0
 
    for key in adj_ps_by_ind:
        x = len(adj_ps_by_ind[key])
 
        ans += x*(x-1)//2
 
    print(ans)
 
 
 
 
 
    