import bisect 
 
n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
 
ans = 0
 
for elem in a:
    pos = bisect.bisect(b, elem)
    # print(f"pos {pos} b {b} elem {elem}")
    if pos == 0:
        ans = max(ans, b[pos] - elem)
        continue
    
    if pos == m:
        ans = max(ans, elem - b[-1])
        continue
    
    res = min(elem - b[pos-1], b[pos] - elem)
    ans = max(ans, res)
 
print(ans)
 