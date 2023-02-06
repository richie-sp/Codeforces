from sys import stdin
input = stdin.readline
 
for c in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(abs(sum(a)))