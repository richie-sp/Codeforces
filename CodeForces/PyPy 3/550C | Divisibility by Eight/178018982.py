"""
Just code any solution for now, copy dp solution. 
"""
from collections import defaultdict, deque
 
n = input()
list_n = [int(x) for x in n]
 
indices_by_digit = defaultdict(list)
 
for ind, dig in enumerate(list_n):
    indices_by_digit[dig].append(ind)
 
possibilities = [num for num in range(0, 1000, 8)]
 
 
def validate(num: int) -> bool:
    prev_ind = -1
    for dig in str(num):
        dig = int(dig)
        if len(indices_by_digit[dig]) == 0:
            return False
 
        ptr = 0
 
        while ptr < len(indices_by_digit[dig]) and indices_by_digit[dig][ptr] <= prev_ind:
            ptr += 1
 
 
        if ptr < len(indices_by_digit[dig]):
            prev_ind = indices_by_digit[dig][ptr]
        else:
            return False
 
    return True
 
ans = None
for pos in possibilities:
    if validate(pos):
        ans = pos
        break
 
if ans is not None:
    print('YES')
    print(ans)
else:
    print('NO')
 