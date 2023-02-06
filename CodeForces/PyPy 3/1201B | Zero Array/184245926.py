from sys import stdin
input = stdin.readline 
 
n = int(input())
 
a = list(map(int, input().split())); s_a = sum(a)
 
if s_a % 2 == 1:
    print('NO')
else:
    a.sort()
    if s_a - a[-1] < a[-1]:
        print('NO')
    else:
        print('YES')