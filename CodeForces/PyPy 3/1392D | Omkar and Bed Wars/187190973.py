from sys import stdin
import math
input = stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    s = [ch for ch in input()[:-1]]
    if len(set(s)) == 1:
        print(int(math.ceil(n / 3))) if n > 2 else print(0); continue
 
    Ls = []; Rs = []; ans = 0
    if s[0] != s[-1]:
        curr = [s[0]]
        for i in range(1, len(s)):
            if s[i] == curr[-1]:
                curr.append(s[i])
            else:
                if curr[-1] == 'L':
                    Ls.append(curr)
                else:
                    Rs.append(curr)
                ans += len(curr) // 3
                curr = [s[i]]
 
        if curr:
            ans += len(curr) // 3
            if curr[-1] == 'L':
                Ls.append(curr)
            else:
                Rs.append(curr)
 
    else:
        l_ch = s[-1]; l_ptr = n - 1; r_ch =s[0]; r_ptr = 0
        while s[l_ptr] == l_ch: l_ptr -= 1
        while s[r_ptr] == r_ch: r_ptr += 1
        l_ptr += 1; r_ptr -= 1
        edge_length = r_ptr + 1 + (n - 1) - l_ptr + 1
        ans += edge_length // 3
        s = s[r_ptr + 1: l_ptr]
 
        curr = [s[0]]
        for i in range(1, len(s)):
            if s[i] == curr[-1]:
                curr.append(s[i])
            else:
                if curr[-1] == 'L':
                    Ls.append(curr)
                else:
                    Rs.append(curr)
                ans += len(curr) // 3
                curr = [s[i]]
 
        if curr:
            ans += len(curr) // 3
            if curr[-1] == 'L':
                Ls.append(curr)
            else:
                Rs.append(curr)
 
    print(ans)