import math
from collections import defaultdict
for case in range(int(input())):
    n = int(input())
    '''
    1 lcm(1, p_1) = 1 => 1
 
    1, 2 .... lcm(1, 2) = 2, lcm(2, 1) = 2 => 4
 
    1 2 3 = 6
 
    1 3 2 = 13
 
    2 1 3 = 11
 
    2 3 1 = 8
 
    3 1 2 = 11
 
    3 2 1
 
    1 2 3 4      4 {3, 1}, 3 {4, 2, 1}, 2 {3, 1} 1 {4, 3, 2, 1}
 
    2 1 4 3
 
    '''
 
    if n % 2 == 0:
        ans = []
        for i in range(1, n // 2 + 1):
            ans.extend([str(2 * i), str(2 * i - 1)])
 
    elif n % 2 == 1:
        ans = [str(1)]
        for i in range(1, n // 2 + 1):
            ans.extend([str(2 * i + 1), str(2 * i)])
 
 
    # coprime_mapping = defaultdict(list)
    # for i in range(n, 0, -1):
    #     for j in range(i, 0, -1):
    #         if math.gcd(i, j) == 1:
    #             if i == j:
    #                 coprime_mapping[i].append(j)
    #                 continue
    #             coprime_mapping[i].append(j)
    #             coprime_mapping[j].append(i)
    # real_mapping = {}
    # found = set()
    # for i in range(n, 0, -1):
    #     ptr = 0
    #     while ptr < len(coprime_mapping[i]) and coprime_mapping[i][ptr] in found:
    #         ptr += 1
 
    #     real_mapping[i] = coprime_mapping[i][ptr]
    #     found.add(real_mapping[i])
 
    # ans = [str(real_mapping[i]) for i in range(1, n + 1)]
 
    print(' '.join(ans))
 
 
 
 