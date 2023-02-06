from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    a, b = input().split('+')
    a, b = int(a), int(b)
 
    print(a + b)