from sys import stdin
input = stdin.readline
 
for c in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    print('bOb') if a[0] <= min(a[1:]) else print('aLicE')