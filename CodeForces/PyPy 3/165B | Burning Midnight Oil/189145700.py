def get_lines(v, k):
    ans = v; curr = v
    while curr // k > 0:
        ans += curr // k
        curr /= k
    return ans
 
n, k = map(int, input().split())
lo = 1; hi = n * k
 
while lo < hi:
    if lo == hi - 1: break
    mid = (lo + hi) // 2
    if get_lines(mid, k) < n:
        lo = mid + 1
    else:
        hi = mid
if get_lines(lo - 1, k) >= n: 
    ans = lo - 1
elif get_lines(lo, k) >= n: 
    ans = lo
elif get_lines(lo + 1, k) >= n: 
    ans = lo + 1
 
print(ans)