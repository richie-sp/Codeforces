from functools import cache
 
class Solution:
    @cache
    def compute(self, p: bool, w: int, b: int) -> int:
        if w == 0 and b == 0:
            return 0
 
        if w < 0 or b < 0: return 0
 
        if p:
            return w/(w + b) * 1 + b/(w + b) * self.compute(not p, w, b - 1)
        else:
            """
            Three scenarios: 
 
            1. Dragon draws w (return 0)
            2. Dragon draws b and b jumps out after
            3. Dragon draws b and w jumps out after
            """
            
 
            try:
                option_2 = b/(w + b) * (b - 1)/(w + b - 1) * self.compute(not p, w, b - 2)
            except: 
                option_2 = 0
 
            try:
                option_3 = b/(w + b) * w/(w + b - 1) * self.compute(not p, w - 1, b - 1)
            except:
                option_3 = 0
 
            return option_2 + option_3
 
            
 
    def solve(self):
        w, b = map(int, input().split())
        ans = self.compute(True, w, b)
        print(ans)
 
 
solution_obj = Solution()
solution_obj.solve()
 