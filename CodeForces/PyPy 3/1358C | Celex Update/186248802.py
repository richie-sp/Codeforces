from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split()); r = y2 - y1; d = x2 - x1; n = r + d
    print(n * (n + 1) // 2 - d * (d + 1) // 2 - r * (r + 1) // 2 + 1)