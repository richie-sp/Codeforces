from sys import stdin
input = stdin.readline
import math
 
for c in range(int(input())):
    n = int(input())
    print(int(math.ceil(n / 2)))
    