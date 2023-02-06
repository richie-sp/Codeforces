from sys import stdin
from collections import defaultdict
from itertools import accumulate
import random
import bisect
input = stdin.readline
 
 
class Solution:
    def stress_test(self):
        for i in range(20000):
            res, a, slow_ans, ans = self.solve()
            if not res:
                print(a, 'hihibyebye', i, slow_ans, ans)
                break
 
    def solve(self):
        n = int(input())
        a = list(map(int, input().split()))
        # a = [random.randint(-5, 5) for i in range(7)]; n = len(a)
 
        arrays = []; curr = []
        for elem in a:
            if elem != 0:
                curr.append(elem)
            else:
                if curr:
                    arrays.append(curr)
                curr = []
        if curr:
            arrays.append(curr)
 
 
 
        ans = 0
        for b in arrays:
            n = len(b); j_by_ind = []
            psum = accumulate(b);
 
            inds_by_val = defaultdict(list)
            for ind, val in enumerate(psum):
                inds_by_val[val].append(ind)
 
            targ = 0
            #deal with first one separately
            for i in range(1, n):
                if b[i] == 0: continue
                targ += b[i - 1]
                if targ not in inds_by_val:
                    ans += n - 1 - i + 1; j_by_ind.append(n - 1)
                    continue
 
                ind = bisect.bisect_right(inds_by_val[targ], i)
                if ind == len(inds_by_val[targ]):
                    j = n - 1
                    to_add = j - i + 1
                else:
                    j = inds_by_val[targ][ind] - 1
                    to_add = j - i + 1
                j_by_ind.append(j)
 
            if 0 in inds_by_val:
                j = inds_by_val[0][0] - 1
                j_by_ind = [j] + j_by_ind
 
            else:
                j_by_ind = [n - 1] + j_by_ind
 
            clean_j_by_ind = [0 for i in range(len(j_by_ind))]; minim = float('inf')
            for i in range(len(j_by_ind) - 1, -1, -1):
                minim = min(minim, j_by_ind[i])
                clean_j_by_ind[i] = minim
 
            
            for i, j in enumerate(clean_j_by_ind):
                diff = j - i + 1
                ans += diff
 
 
        print(ans)
 
                
    
 
 
        # slow_ans = 0
        # for i in range(len(a)):
        #     for j in range(i, len(a)):
        #         subarr = a[i: j + 1]
        #         valid = True
        #         for x in range(len(subarr)):
        #             if not valid: break
        #             for y in range(x, len(subarr)):
        #                 if sum(subarr[x: y + 1]) == 0:
        #                     valid = False; break
        #         if valid: slow_ans += 1
 
        # if slow_ans != ans:
        #     return False, a, slow_ans, ans
        # else:
        #     return True, a, slow_ans, ans
 
 
solution_obj = Solution()
solution_obj.solve()
 
    