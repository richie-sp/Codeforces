from sys import stdin 
input = stdin.readline 
 
for case in range(int(input())):
    s = [int(ch) for ch in input()[:-1]]
    w = [None for ch in s]
    x = int(input())
 
    for ind, ch in enumerate(s):
        l = ind - x; r = ind + x
        if ch == 1:
            if l >= 0: 
                if w[l] is None: w[l] = 1
            if r < len(s):
                if w[r] is None: w[r] = 1
        else:
            if l >= 0: w[l] = 0
            if r < len(s): w[r] = 0
    ans = True
    for ind, ch in enumerate(s):
        l = ind - x; r = ind + x
        if ch == 1:
            okay = False
            if l >= 0:
                if w[l] in [1, None]: okay = True
            if r < len(s):
                if w[r] in [1, None]: okay = True
            if not okay: 
                ans = False; break
        else:
            okay = True
            if l >= 0: 
                if w[l] == 1: okay = False
            if r < len(s):
                if w[r] == 1: okay = False
            if not okay:
                ans = False; break
 
    if not ans:
        print(-1); continue
 
    ans = []
    for ch in w:
        if ch is None:
            ans.append('1')
        else:
            ans.append(str(ch))
 
    print(''.join(ch for ch in ans))