from sys import stdin
input = stdin.readline
 
for c in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    sorted_s = list(sorted(s))
 
    ans = []
    for e in s:
        if e != sorted_s[-1]:
            ans.append(str(e - sorted_s[-1]))
        else:
            ans.append(str(e - sorted_s[-2]))
 
 
    print(' '.join(ans))
 