from typing import List
 
def merge_info(a: List[List[int]]) -> List[List[int]]:
    new_a = []
    for ind, info in enumerate(a):
        if ind == 0:
            new_a.append(info)
        else:
            if info[0] == new_a[-1][0]:
                new_a[-1][1] += info[1]
            else:
                new_a.append(info)
 
    return new_a
 
 
 
 
 
 
t = int(input())
 
for case in range(t):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    k = int(input())
    b = [int(x) for x in input().split()]
 
    ans = False
    count = 1
    min_ind = 0
    # print(f"Original a {a} Original b {b}")
    a_info = []
    for ind, num in enumerate(a):
        exp = 0
        while num % m == 0:
            num /= m
            exp += 1
 
        
        a_info.append([int(num), m ** exp])
 
    b_info = []
    for ind, num in enumerate(b):
        exp = 0
        while num % m == 0:
            num /= m
            exp += 1
 
        b_info.append([int(num), m ** exp])
 
    # print(merge_info(a_info), merge_info(b_info))
 
    # print(f"a_info {a_info} b_info {b_info}")
 
    print('Yes') if merge_info(a_info) == merge_info(b_info) else print('No')
 
    
    
 
 
    
 
    
 
    