from sys import stdin
input = stdin.readline
 
for case in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    curr_segment = []; segments = []; comp_segment = []; comp_segments = []
    for ind, num in enumerate(a):
        adj_ind = ind + 1
        if num == adj_ind:
            curr_segment.append(num)
            if comp_segment: comp_segments.append(comp_segment)
            comp_segment = []
        else:
            if curr_segment: segments.append(curr_segment)
            comp_segment.append(num); curr_segment = []
 
    if curr_segment: segments.append(curr_segment)
    if comp_segment: comp_segments.append(comp_segment)
 
    if not comp_segments:
        print(0); continue
 
    if len(comp_segments) == 1:
        print(1); continue
 
    print(2)