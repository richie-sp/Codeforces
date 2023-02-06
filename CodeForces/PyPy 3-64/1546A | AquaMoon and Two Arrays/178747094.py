from collections import defaultdict 
 
for c in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
 
    if sum(a) != sum(b):
        print(-1)
        continue
 
    count_by_ind = {}
 
    for i in range(len(a)):
        count_by_ind[i + 1] = b[i] - a[i]
 
    i_s, j_s = [], []
 
    for i, c in count_by_ind.items():
        if c > 0:
            i_s.extend([i] * c)
        if c < 0:
            j_s.extend([i] * (-c))
 
    print(len(i_s))
    for i, j in zip(i_s, j_s):
        print(j, i)
        
 
    # print(count_by_ind)
 
    # print(i_s)
    # print(j_s)
 
    