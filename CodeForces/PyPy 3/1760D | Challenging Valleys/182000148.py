from sys import stdin
input = stdin.readline
 
for c in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print('yES')
        continue
    clean_a = []; prev = float('inf')
    for e in a:
        if e == prev:
            continue
        clean_a.append(e)
        prev = e
 
    if len(clean_a) == 1:
        print('yEs')
        continue
 
    valleypoints = []
    for i, e in enumerate(clean_a):
        if i == 0:
            if clean_a[i] >= clean_a[i + 1]:
                continue
            else:
                valleypoints.append(clean_a[i])
        elif i == len(clean_a) - 1:
            if clean_a[i] >= clean_a[i - 1]:
                continue
            else:
                valleypoints.append(clean_a[i])
        else:
            if clean_a[i] < min(clean_a[i - 1], clean_a[i + 1]):
                valleypoints.append(clean_a[i])
 
 
 
    print('yEs') if len(valleypoints) == 1 else print('nO')