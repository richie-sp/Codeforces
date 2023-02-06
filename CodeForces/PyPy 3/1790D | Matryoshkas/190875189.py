from sys import stdin
from collections import Counter
import math
input = stdin.readline
 
for case in range(int(input())):
    n = input()
    a = list(map(int, input().split())); a.sort()
 
    segments = []; curr_segment = []; curr = None
 
    for elem in a:
        if curr is None:
            curr = elem
            curr_segment = [elem]
            continue
 
        if curr == elem or curr == elem - 1:
            curr = elem
            curr_segment.append(elem)
            continue
        
        if curr_segment:
            segments.append(curr_segment)
        curr = elem
        curr_segment = [elem]
 
    if curr_segment:
        segments.append(curr_segment)
 
    ans = 0
    for seg in segments:
        cts = list(Counter(seg).values())
        prev_min = 0; prev_max = float('-inf')
        seg_ans = 0; added_end = False; added_prev_max = False
        for i in range(len(cts)):
            if i == 0:
                prev_min = cts[i]; prev_max = cts[i]; continue
 
            if cts[i] > cts[i - 1]:
                seg_ans += cts[i] - cts[i - 1]
                if i == len(cts) - 1: added_end = True
                if not added_prev_max:
                    seg_ans += prev_max; added_prev_max = True
                
 
            prev_max = max(prev_max, cts[i])
 
        if not added_end and not added_prev_max: seg_ans += prev_max
        ans += seg_ans
 
    print(ans)
 
        
 
        