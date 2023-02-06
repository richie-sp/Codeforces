from sys import stdin
import math
input = stdin.readline 
 
for c in range(int(input())):
    n, k = map(int, input().split())
    s = [ch for ch in input()[:-1]]; s.sort()
    if k == n:
        print(s[-1]); continue
 
    strings = [[] for i in range(k)]
    for i in range(k):
        strings[i].append(s[i])
 
    if strings[-1][0] != strings[0][0]:
        print(strings[-1][0]); continue
 
    #now we assume that all the elements are the same originally
    #so we reduce problem to finding lexicographically smallest string
 
    if s[k] == s[-1]:
        size = n - 1 - k + 1
        maxim = int(math.ceil(size / k))
        print(strings[0][0] + s[k] * maxim)
        continue 
 
    print(strings[0][0] + ''.join(s[k:]))
    