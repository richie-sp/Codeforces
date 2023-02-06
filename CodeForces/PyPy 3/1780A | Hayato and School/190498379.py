from sys import stdin
from math import ceil
input = stdin.readline
 
for case in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    odd_indices = []; even_indices = []
 
    for ind, num in enumerate(a):
        if num % 2 == 1:
            odd_indices.append(ind + 1)
        else:
            even_indices.append(ind + 1)
 
    if len(odd_indices) >= 3:
        print('YES')
        print(f'{str(odd_indices[0])} {str(odd_indices[1])} {str(odd_indices[2])}')
    elif len(odd_indices) >= 1 and len(even_indices) >= 2:
        print('YES')
        print(f'{str(odd_indices[0])} {str(even_indices[0])} {str(even_indices[1])}')
    else:
        print('NO')