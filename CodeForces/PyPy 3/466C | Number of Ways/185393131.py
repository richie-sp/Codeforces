from sys import stdin
import bisect
input = stdin.readline
 
n = int(input())
a = list(map(int, input().split()))
 
if len(a) < 3:
    print(0)
elif sum(a) % 3 != 0:
    print(0)
else:
    targ = sum(a) // 3
    if targ == 0:
        #you can't use point at end as cutoff
        i_inds = []; curr_sum = 0
        for i in range(n - 1):
            curr_sum += a[i]
            if curr_sum == 0:
                i_inds.append(i)
 
        k = len(i_inds)
        print(k * (k - 1) // 2)
    else:
        t_1 = targ; t_2 = targ * 2; curr_sum = 0; i_inds = []; j_inds = []
        for i in range(n - 1):
            curr_sum += a[i]
            if curr_sum == t_1:
                i_inds.append(i)
            if curr_sum == t_2:
                j_inds.append(i)
        ans = 0
        for e in i_inds:
            ind = bisect.bisect_right(j_inds, e)
            ans += len(j_inds) - ind
 
        print(ans)
 