for case in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    sorted_a = sorted(a)
 
    min_a = sorted_a[0]
    min_ans = min_a
 
    for ind, val in enumerate(sorted_a):
        if ind == 0:
            continue
        if sorted_a[ind] > sorted_a[ind - 1]:
            min_ans += sorted_a[ind] - sorted_a[ind - 1]
 
 
    actual_ans = a[0]
 
    for ind, val in enumerate(a):
        if ind == 0:
            continue
        if a[ind] > a[ind - 1]:
            actual_ans += a[ind] - a[ind - 1]
 
    if min_ans == actual_ans:
        print('YES')
    else:
        print('NO')
 