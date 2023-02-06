from sys import stdin
from collections import defaultdict
import string
input = stdin.readline
 
for c in range(int(input())):
    n = int(input())
    s = input()[:-1]
 
    ind_by_combo = defaultdict(lambda: float('-inf'))
    ans = False
    for i in range(1, len(s)):
        curr = s[i - 1: i + 1]
        if curr not in ind_by_combo:
            ind_by_combo[curr] = i - 1
        else:
            if i - 1 - ind_by_combo[curr] > 1:
                ans = True; break
 
    print('YES') if ans else print('NO')
 