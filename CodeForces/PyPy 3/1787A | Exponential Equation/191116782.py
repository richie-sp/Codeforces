from sys import stdin
input = stdin.readline
 
for case in range(int(input())):
    n = int(input())
 
    if n % 2 == 0:
        print(str(n // 2) + ' ' + '1')
    else:
        print('-1')