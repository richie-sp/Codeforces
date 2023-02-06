from sys import stdin
from math import log10, ceil
input = stdin.readline
 
for case in range(int(input())):
    
    n, s = map(str, input().split()); int_n = int(n)
    if sum(int(ch) for ch in n) <= int(s):
        print(0); continue 
 
    n = [ch for ch in n]; 
    candidate_ans = []; candidate_np = []
    for i in range(len(n) - 1, -1, -1):
        curr = ''.join(n[i:])
        inc = 10 ** (len(n) - 1 - i + 1) - int(curr)
        candidate_ans.append(inc)
        cand_np = int_n + inc
        sum_digs = sum(int(ch) for ch in str(cand_np))
        if sum_digs <= int(s):
            print(inc); break