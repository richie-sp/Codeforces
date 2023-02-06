from decimal import Decimal
import datetime
from functools import cache
class Solution:
    @cache
    def compute_ev(self, c, m, p, v) -> int:
        ans = 1
        #only compute probability from c if c > 0...else no need to compute
        if c > 0:
            if c > v:
                red_c = v
            else:
                red_c = c
 
            if m != 0 and p != 0:
                new_c, new_m, new_p = max(0, c - v), m + red_c / 2, p + red_c / 2
            elif m != 0:
                new_c, new_m, new_p = max(0, c - v), m + red_c, p
            elif p != 0:
                new_c, new_m, new_p = max(0, c - v), m, p + red_c
 
            ans += c * self.compute_ev(new_c, new_m, new_p, v)
 
 
        #mirror case below to the above
        if m > 0:
            if m > v:
                red_m = v
            else:
                red_m = m
 
            if c != 0 and p != 0:
                new_c, new_m, new_p = c + red_m / 2, max(0, m - v), p + red_m / 2
            elif c != 0:
                new_c, new_m, new_p = c + red_m, max(0, m - v), p
            elif p != 0:
                new_c, new_m, new_p = c, max(0, m - v), p + red_m
 
            ans += m * self.compute_ev(new_c, new_m, new_p, v)
 
        return ans
 
# t1 = datetime.datetime.now()
solution_obj = Solution()
for case in range(int(input())):
    c, m, p, v = [Decimal(x) for x in input().split()]
    
    print(solution_obj.compute_ev(c, m, p, v))
 
# t2 = datetime.datetime.now()
# print(t2 - t1)
 
 
 
 
    
 