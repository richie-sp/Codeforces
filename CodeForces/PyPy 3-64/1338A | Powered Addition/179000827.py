from random import randint
import math
 
from sys import stdin
input = stdin.readline
 
# L = []
# for i in range(15):
#     L.append(randint(1, 50))
 
for case in range(int(input())):
    n = int(input())
    L = list(map(int, input().split()))
 
 
    smallests, smallest = [0 for e in L], L[-1]
    for i in range(len(L) - 2, -1, -1):
        smallests[i + 1] = smallest
        smallest = min(smallest, L[i])
    smallests[0] = smallest
 
    ans = 0
    for x, y in zip(L, smallests):
        if y < x: ans = max(ans, 1 + int(math.log(x - y, 2)))
 
 
    print(ans)