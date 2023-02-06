from collections import defaultdict
 
t = int(input())
for case in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
 
    highest_by_mod = defaultdict(int)
 
    for ind, elem in enumerate(a):
        mod = ind % k
        highest_by_mod[mod] = max(elem, highest_by_mod[mod])
 
    
    ans = 0
    for i in range(k):
        ans += highest_by_mod[i]
 
    print(ans)