from sys import stdin
input = stdin.readline
 
for case in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    o_count = 0; e_count = 0; ans = 0
    for elem in a:
        if elem % 2 == 0:
            e_count += 1; ans += max(o_count - 1, 0)
            o_count = 0
 
        else:
            o_count += 1; ans += max(e_count - 1, 0)
            e_count = 0
 
    ans += max(o_count - 1, 0) + max(e_count - 1, 0)
 
    print(ans)