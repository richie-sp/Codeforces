from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    x1, x2 = map(int, input().split())
    x3, x4 = map(int, input().split())
    ans = False
    for a, b, c, d in [(x1, x2, x3, x4), (x3, x1, x4, x2), (x4, x3, x2, x1), (x2, x4, x1, x3)]:
        if a < b and c < d and a < c and b < d:
            ans = True; break
 
    print('yEs') if ans else print('nO')