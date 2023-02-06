from sys import stdin
input = stdin.readline 
 
for _ in range(int(input())):
    n = int(input()); x = list(map(int, input().split())); t = list(map(int, input().split())); k1 = float('-inf'); k2 = float('-inf')
    for xi, ti in zip(x, t):
        k1 = max(k1, ti + xi); k2 = max(k2, ti - xi)
    print((k1 - k2) / 2)
 