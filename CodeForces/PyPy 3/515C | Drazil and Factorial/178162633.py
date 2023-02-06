import math
from typing import List
 
class Solution:
    def __init__(self, target: int, factorials: List[int]):
        self.target = target
        self.factorials = factorials
        self.ans = None
        self.found = False
 
    def backtrack(self, curr_num: List[int], target: int):
        if self.ans is not None:
            return
 
        if target == 1:
            self.ans = curr_num
 
        starting = float('-inf')
        if target % 3 == 0:
            starting = math.factorial(3)
 
        if target % 5 == 0:
            starting = math.factorial(5)
 
        if target % 7 == 0:
            starting = math.factorial(7)
 
 
        for i, fac in self.factorials:
            if fac < starting:
                continue
            if target % fac == 0:
                self.backtrack([*curr_num, i], target // fac)
 
 
    def compute_max(self):
        starting = []
        while self.target % 7 == 0:
            starting.append(7)
            self.target //= math.factorial(7)
 
        while self.target % 5 == 0:
            starting.append(5)
            self.target //= math.factorial(5)
 
 
        self.backtrack(starting, self.target)
 
    
 
n = int(input())
a = input()
 
target = 1
 
for digit in a:
    target *= math.factorial(int(digit))
 
factorials = [[i, math.factorial(i)] for i in range(2, 10)]
 
solution_obj = Solution(target, factorials)
solution_obj.compute_max()
solution_obj.ans.sort(reverse = True)
print(''.join(str(digit) for digit in solution_obj.ans))