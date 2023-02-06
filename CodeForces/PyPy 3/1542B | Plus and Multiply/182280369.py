"""
Come back to this
"""
from sys import stdin
 
input = stdin.readline
 
 
for case in range(int(input())):
    n, a, b = map(int, input().split())
 
 
    curr = 1; ans = False; prev = float('-inf')
    while curr <= n:
        if prev == curr:
            break
        if (n - curr) % b == 0:
            ans = True
            break
        prev = curr
        curr *= a
 
 
    print('yEs') if ans else print('nO')
 
 
 
 
    
 
 
    
 
 