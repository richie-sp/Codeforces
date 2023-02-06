for case in range(int(input())):
    n = int(input())
    x = [int(a) for a in input().split()]
    max_diff = x[-1] - x[0] + 2
    min_diff = x[-1] - x[0] - 2
 
    if not min_diff + 1 <= len(x) <= max_diff + 1:
        print('NO')
        continue
 
    max_consc = 0
    curr_consc = 0
    ans = True
    for i in range(1, len(x)):
        if x[i] - x[i-1] > 3:
            ans = False
            curr_consc = 0
        elif x[i] - x[i-1] == 2:
            curr_consc += 1
        else:
            curr_consc = 0
 
        max_consc = max(max_consc, curr_consc)
        if max_consc > 2:
            ans = False
 
    print('YES') if ans else print('NO')