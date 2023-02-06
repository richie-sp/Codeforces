"""
Accepted: Precomputation Solution
Read DP Solution....going to code different solution which utilizes precomputation
*Edit*: Turns out my precomputation solution and DP solution are actually the same
"""
from sys import stdin
input = stdin.readline
 
n = int(input())
a = list(map(int, input().split()))
 
if n <= 2:
    print(n)
else:
    curr = [a[0]]; prev = a[0]; segments = []
    for i in range(1, n):
        if a[i] > prev:
            curr.append(a[i])
        else:
            segments.append(curr)
            curr = [a[i]]
        prev = a[i]
    segments.append(curr)
 
    curr_seg = 0; seg_ind = 0; global_ind = 0; endings = [1 for i in range(n)]; startings = [1 for i in range(n)]
    while global_ind < n:
        startings[global_ind] = len(segments[curr_seg]) - seg_ind
        endings[global_ind] = seg_ind + 1
        seg_ind += 1; global_ind += 1
        if seg_ind == len(segments[curr_seg]): 
            seg_ind = 0; curr_seg += 1
 
    def get_startings(i: int):
        if 0 <= i < len(startings): return startings[i]
        return 0
 
    def get_endings(i: int):
        if 0 <= i < len(endings): return endings[i]
        return 0
 
    ans = 2
    for i in range(n):
        curr1 = 1; curr2 = 1;
        #case 1. a[i] = a[i - 1] + 1 ...
        try: 
            if a[i - 1] + 1 > a[i - 1]: curr1 += get_endings(i - 1)
        except: pass
        try:
            if a[i - 1] + 1 < a[i + 1]: curr1 += get_startings(i + 1)
        except: pass
 
        #case 2. a[i] = a[i + 1] - 1 ...
        try:
            if a[i + 1] - 1 > a[i - 1]: curr2 += get_endings(i - 1)
        except: pass
        try:
            if a[i + 1] - 1 < a[i + 1]: curr2 += get_startings(i + 1)
        except: pass
 
        ans = max(ans, curr1, curr2)
 
    print(ans)
        
            
       
 
 
 
    
 
 
 
 
 
 