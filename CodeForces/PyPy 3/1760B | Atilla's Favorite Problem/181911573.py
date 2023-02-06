from sys import stdin
input = stdin.readline
 
for c in range(int(input())):
    n = int(input())
    s = input()
 
    ans = float('-inf')
    for e in s:
        ans = max(ans, ord(e) - 96)
 
    print(ans)