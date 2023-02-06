from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    k, n = map(int, input().split())
 
    ans = [1]; rem = k - 1; spacings = set()
    for sp in range(1, n + 1):
        if ans[-1] == n or len(ans) == k:
            break
        if sp not in spacings and ans[-1] + sp <= n - (k - (len(ans) + 1)):
            ans.append(ans[-1] + sp)
            spacings.add(sp)
        else:
            ans.append(ans[-1] + 1)
 
    print(' '.join([str(ch) for ch in ans]))