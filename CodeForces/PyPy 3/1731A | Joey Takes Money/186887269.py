from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    prod = 1
    for elem in a:
        prod *= elem
 
    print((prod + (len(a) - 1)) * 2022)