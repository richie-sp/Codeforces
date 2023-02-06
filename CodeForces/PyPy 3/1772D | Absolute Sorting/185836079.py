from sys import stdin
import math
input = stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    ub = float('inf'); lb = float('-inf')
    for i in range(1, len(a)):
        prev, curr = a[i - 1], a[i]
        if curr > prev:
            ub = min(ub, (prev + curr) // 2)
        elif curr < prev:
            lb = max(lb, int(math.ceil((prev + curr) / 2)))
 
    if lb > ub:
        print(-1)
    else:
        print(max(lb, 0))