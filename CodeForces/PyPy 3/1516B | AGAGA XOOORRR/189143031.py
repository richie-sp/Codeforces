from sys import stdin
input = stdin.readline
 
for case in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
 
    base = a[0]; pxor = [a[0]]
    for i in range(1, len(a)):
        base ^= a[i]; pxor.append(base)
 
    if base == 0:
        print('YES')
    else:
        base = a[0]; ans = False
        for i in range(1, n):
            #check if a[i:] is valid (aka xor of everything from a[i:] is 0 and that you have base in this prefix)
            if pxor[-1] ^ pxor[i - 1] == 0:
                for j in range(i + 1, n):
                    if pxor[-1] ^ pxor[j - 1] == base:
                        ans = True; break
            base ^= a[i]
 
        print('YES') if ans else print('NO')