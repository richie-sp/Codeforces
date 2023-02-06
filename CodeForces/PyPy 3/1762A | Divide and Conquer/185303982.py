from sys import stdin
input = stdin.readline
 
for case in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    if sum(a) % 2 == 0:
        print(0); continue 
 
    ans = float('inf')
    for elem in a:
        if elem % 2 == 1:
            e = elem; ops = 0
            while e % 2 == 1:
                e //= 2; ops += 1
 
            ans = min(ans, ops)
        else:
            e = elem; ops = 0
            while e % 2 == 0:
                e //= 2; ops += 1
            ans = min(ans, ops)
 
 
    print(ans)