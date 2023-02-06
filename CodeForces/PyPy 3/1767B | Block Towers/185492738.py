from sys import stdin
import math
input = stdin.readline
 
for case in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = a[0]; a = a[1:]; a.sort()
 
    for elem in a:
        if elem <= ans:
            continue
        ans = int(math.ceil((ans + elem) / 2))
 
    print(ans)