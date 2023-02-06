from sys import stdin
import itertools
input = stdin.readline
 
n = int(input())
s = input()[:-1]
 
 
zero_ct = 0; one_ct = 0
for elem in s:
    if elem == '0':
        zero_ct += 1
    else:
        one_ct += 1
 
 
num_lower = 2 ** one_ct - 1; num_higher = 2 ** zero_ct - 1
 
lo = num_lower + 1; hi = 2 ** n - num_higher
 
 
ans = [str(i) for i in range(lo, hi + 1)]
print(' '.join(ans))