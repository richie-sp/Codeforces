n = int(input())
 
if n <= 2:
    print(2 * n + 1)
else:
    print(7 + n % 3 + 4 * (n // 3 - 1))