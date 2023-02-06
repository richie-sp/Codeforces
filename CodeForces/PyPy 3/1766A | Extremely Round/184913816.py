from sys import stdin
input = stdin.readline
 
for c in range(int(input())):
    n = int(input())
    if n < 10:
        print(n)
    elif 10 <= n <= 99:
        print(9 + n // 10)
    elif 100 <= n <= 999:
        print(9* 2 + n // 100)
    elif 1000 <= n <= 9999:
        print(9 * 3 + n // 1000)
    elif 10000 <= n <= 99999:
        print(9 * 4 + n // 10000)
    else:
        print(9 * 5 + n // 100000)
    
 
    