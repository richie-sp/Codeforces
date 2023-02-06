import math
k = int(input())
avg = k ** 0.1; hi = int(math.ceil(avg)); lo = int(avg)
 
maxim = hi ** 10; lo_ct = 0
for i in range(11):
    if hi ** (10 - i) * lo ** i >= k:
        hi_ct = 10 - i; lo_ct = i
    else:
        break
 
ans = []
for ind, elem in enumerate('codeforces'):
    if ind + 1 <= lo_ct:
        ans.append(elem * lo)
    else:
        ans.append(elem * hi)
 
print(''.join(ans))