from typing import List
import copy, itertools
 
class Solution:
    def __init__(self, arr: List[int]) -> None:
        self.arr = arr
        pe_sum, po_sum = [arr[0]], [0]
        for i in range(1, len(arr)):
            if i % 2 == 0:
                pe_sum.append(pe_sum[-1] + arr[i])
                po_sum.append(po_sum[-1])
            else:
                pe_sum.append(pe_sum[-1])
                po_sum.append(po_sum[-1] + arr[i])
 
        self.pe_sum, self.po_sum = pe_sum, po_sum
 
    def get_pe_sum(self, i: int) -> int:
        if i < 0:
            return 0
        return self.pe_sum[i]
 
    def get_po_sum(self, i: int) -> int:
        if i < 0:
            return 0
        return self.po_sum[i]
 
    def solve(self) -> int:
        n = len(self.arr)
        
        dp = [0] * (n + 1)
 
 
        for i in range(n - 2, -1, -1):
            #Option 1: Swap i with i + 1 only, leave i + 2, .....
            #Option 2: Swap i with i + 1 and i + 2,.... i + k
            if i % 2 == 0:
                option_1 = self.arr[i + 1] + self.get_pe_sum(n - 1) - self.get_pe_sum(i + 1)
                option_2 = self.arr[i + 1] + dp[i + 2]
            else:
                option_1 = self.arr[i] + self.get_pe_sum(n - 1) - self.get_pe_sum(i + 1)
                option_2 = self.arr[i] + dp[i + 2]
 
            dp[i] = max(option_1, option_2)
 
        ans = self.get_pe_sum(n - 1)
 
        for i in range(len(dp)):
            ans = max(ans, dp[i] + self.get_pe_sum(i - 1))
        
        return ans
 
 
    def solve_slow(self) -> int:
        ans = sum(self.arr[i] for i in range(len(self.arr)) if i % 2 == 0)
        expected_dp = [0]
        for l in range(len(self.arr)):
            for r in range(l + 1, len(self.arr)):
                arr = copy.copy(self.arr)
                window = arr[l:r + 1]
 
                for i in range(l, r + 1):
                    arr[i] = window.pop()
                
                ans = max(ans, sum(arr[i] for i in range(len(arr)) if i % 2 == 0))
 
        return ans
 
 
    
 
    
for case in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
 
    # all_perms = list(itertools.permutations(arr))
 
    # for perm in all_perms:
    #     solution_obj = Solution(list(perm))
    #     ans1 = solution_obj.solve()
    #     ans2 = solution_obj.solve_slow()
 
 
    #     if ans1 != ans2:
    #         print(list(perm), ans1, ans2)
    #         break
 
    solution_obj = Solution(arr)
    ans1 = solution_obj.solve()
    # ans2 = solution_obj.solve_slow()
 
    print(ans1)
    
 
    
 
    
 
 