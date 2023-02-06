from sys import stdin
input = stdin.readline 
 
for case in range(int(input())):
    words = []
    n = int(input())
    As = []; Bs = []; Cs = []; Ds = []; Es = []
    for line in range(n):
        word = input()[:-1]
        a_ct = 0; b_ct = 0; c_ct = 0; d_ct = 0; e_ct = 0
        for ch in word:
            if ch == 'a':
                a_ct += 1
            if ch == 'b':
                b_ct += 1
            if ch == 'c':
                c_ct += 1
            if ch == 'd':
                d_ct += 1
            if ch == 'e':
                e_ct += 1
 
        a_delta = a_ct - (len(word) - a_ct)
        b_delta = b_ct - (len(word) - b_ct)
        c_delta = c_ct - (len(word) - c_ct)
        d_delta = d_ct - (len(word) - d_ct)
        e_delta = e_ct - (len(word) - e_ct)
 
        As.append(a_delta)
        Bs.append(b_delta)
        Cs.append(c_delta)
        Ds.append(d_delta)
        Es.append(e_delta)
 
    As.sort(); Bs.sort(); Cs.sort(); Ds.sort(); Es.sort()
 
    ans = 0
    for L in [As, Bs, Cs, Ds, Es]:
        curr_sum = 0
        for i in range(n - 1, -1, -1):
            curr_sum += L[i]
            if curr_sum > 0:
                ans = max(ans, (n - 1) - i + 1)
 
    print(ans)