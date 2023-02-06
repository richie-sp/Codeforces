from sys import stdin
input = stdin.readline
 
n = int(input())
arr = list(map(int, input().split()))
 
if n == 1:
    print(1, 0)
else:
    l = 0; r = n - 1; lsum = arr[0]; rsum = arr[-1]
 
    while l < r:
        if l == r - 1: break
        if lsum <= rsum:
            l += 1
            lsum += arr[l]
        else:
            r -= 1
            rsum += arr[r]
 
    print(l + 1, n - (l + 1))