from sys import stdin
input = stdin.readline
import math
 
for case in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mapping = [(a[ind], ind) for ind in range(len(a))]
 
    mapping.sort(); mult = mapping[0][0]; p = 0; operations = []
    for i in range(1, len(a)):
        #find the next multiple of mult which is greater than a[i]
        if mult % mapping[i][0] == 0:
            continue
 
        if mult > mapping[i][0]:
            operations.append([str(mapping[i][1] + 1), str(mult - mapping[i][0])]); p += 1
            continue 
        #mult < a[i]
        k = int(math.ceil(mapping[i][0] / mult))
        mult *= k
 
        operations.append([str(mapping[i][1] + 1), str(mult - mapping[i][0])]); p += 1
 
    print(p)
    for e in operations:
        print(f"{e[0]} {e[1]}")
 
 
        