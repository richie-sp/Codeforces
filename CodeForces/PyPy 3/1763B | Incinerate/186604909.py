from sys import stdin
input = stdin.readline
import bisect
 
 
for _ in range(int(input())):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    p = list(map(int, input().split()))
 
    info = [(hi, pi) for hi, pi in zip(h, p)]; info.sort(); min_by_ind = [float('inf') for i in range(n)]; min_by_ind[-1] = info[-1][1]
    for i in range(n - 2, -1 , -1):
        min_by_ind[i] = min(min_by_ind[i + 1], info[i][1])
 
 
    cut_ind = 0; i = 0; ans = False; prev_cumu_k = 0; cumu_k = k
    #modify termination condition
    while prev_cumu_k != cumu_k and cut_ind < n:
        cut_ind = bisect.bisect_right(info, (cumu_k, float('inf')))
        if cut_ind == n:
            ans = True; break
        prev_cumu_k = cumu_k
        k -= min_by_ind[cut_ind]; k = max(k, 0); cumu_k += k
        i += 1
    if cut_ind == n: ans = True
 
    print('YES') if ans else print('NO')