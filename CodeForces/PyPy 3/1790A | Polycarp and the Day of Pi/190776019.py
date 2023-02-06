from sys import stdin
import math
input = stdin.readline
 
for case in range(int(input())):
    n = input()
    pi = '31415926535897932384626433832795028841971693993751058209749445923078164'[:30]
    ans = 0
    for i in range(min(len(n), len(pi))):
        if n[i] == pi[i]:
            ans += 1
        else:
            break
 
    print(ans)