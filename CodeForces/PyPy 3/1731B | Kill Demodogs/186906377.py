from sys import stdin
input = stdin.readline
 
md = 10 ** 9 + 7
 
 
for _ in range(int(input())):
    n = int(input())
    
    print(((n - 1) * n * (n + 1)//3 + n * (n + 1) * (2*n + 1)//6) * 2022 % md)
 
    