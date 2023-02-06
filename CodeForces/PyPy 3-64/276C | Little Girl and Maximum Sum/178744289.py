"""
Seems like we can use a segment tree
"""
from sys import stdin
input=stdin.readline
 
n, q = map(int, input().split())
a = sorted(map(int, input().split()))
 
arr = [0] * n
for line in range(q):
    l, r = map(int, input().split())
    arr[l - 1] += 1
    if r < len(arr): arr[r] -= 1
 
for i in range(1, n):
    arr[i] = arr[i] + arr[i - 1]
 
arr.sort()
 
print(sum(x*y for x, y in zip(a, arr)))
 
 
 
 
 