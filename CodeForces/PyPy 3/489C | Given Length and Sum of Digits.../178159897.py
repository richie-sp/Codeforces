from typing import List, Deque
from collections import deque
 
class Solution:
    def __init__(self):
        self.min_num, self.max_num  = None, None
    
    def gen_min_num(self, digits: int, target_sum: int, curr_num: Deque[int]):
        #You simply require that if digits > 1, you add the maximum digit possible such that you have at least one left
        if digits == 0: 
            if target_sum == 0:
                self.min_num = int(''.join(str(dig) for dig in curr_num))
        else:
            for i in range(9, -1, -1):
                nex_target_sum = target_sum - i
 
                if nex_target_sum < 0:
                    continue
 
                if nex_target_sum == 0 and digits - 1 == 0:
                    self.gen_min_num(digits - 1, nex_target_sum, deque([i, *curr_num]))
                    break
 
                if nex_target_sum > 0 and digits - 1 > 0:
                    self.gen_min_num(digits - 1, nex_target_sum, deque([i, *curr_num]))
                    break
 
 
    def gen_max_num(self, digits: int, target_sum: int, curr_num: List[int]):
        if digits == 0: 
            if target_sum == 0:
                self.max_num = int(''.join(str(dig) for dig in curr_num))
        else:
            for i in range(9, -1, -1):
                if i == 0 and digits == self.digits and self.digits != 1:
                    break
                if target_sum >= i:
                    self.gen_max_num(digits - 1, target_sum - i, [*curr_num, i])
                    break
 
 
                
 
 
 
m, s = [int(x) for x in input().split()]
solution_obj = Solution()
solution_obj.digits = m
solution_obj.gen_min_num(m, s, deque([]))
solution_obj.gen_max_num(m, s, [])
 
 
if solution_obj.min_num is None: solution_obj.min_num = -1
 
if solution_obj.max_num is None: solution_obj.max_num = -1
 
 
print(f"{solution_obj.min_num} {solution_obj.max_num}")
 