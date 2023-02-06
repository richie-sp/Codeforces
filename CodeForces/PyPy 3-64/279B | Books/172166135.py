n, t = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
 
 
l, r = 0, 0
#l <= r ALWAYS
ans = 0
curr_t = 0
max_books = 0
while l < n:
    r = max(r, l)
    if l == r and a[l] > t:
        l += 1
        r += 1
        continue
 
    if l == r:
        curr_t = a[l]
 
    while r + 1 < n and curr_t + a[r+1] <= t:
        curr_t += a[r+1]
        r += 1
 
    max_books = max(max_books, r - l + 1)
    curr_t -= a[l]
    l += 1
    
 
print(max_books)
 