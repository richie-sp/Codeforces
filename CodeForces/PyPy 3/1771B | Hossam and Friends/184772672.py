from sys import stdin
from typing import List, Tuple
from collections import defaultdict
import itertools
import bisect
input = stdin.readline
 
class Solution:
    def __init__(self):
        for c in range(int(input())):
            n, m = map(int, input().split())
            pairs = []; min_by_ind = defaultdict(lambda: n + 1)
            for l in range(m):
                x, y = map(int, input().split())
                if x > y:
                    x, y = y, x
                pairs.append((x, y)); min_by_ind[x] = min(min_by_ind[x], y)
 
            self.fast_solve(n, m, pairs)
    def fast_solve(self, n, m, pairs):
        min_by_ind = defaultdict(lambda: n + 1)
        for p in pairs:
            x, y = p
            if x > y:
                x, y = y, x
            min_by_ind[x] = min(min_by_ind[x], y)
 
        first_bad_index = defaultdict(lambda: n + 1)
        prev_min = n + 1
        for i in range(n, 0, -1):
            first_bad_index[i] = min(min_by_ind[i], prev_min)
            prev_min = min(first_bad_index[i], prev_min)
 
        # print(first_bad_index)
        ans = 0
        for i in range(1, n + 1):
            j = first_bad_index[i] - 1
            ans += (j - i + 1)
 
        print(ans)
 
        return ans
 
 
 
    def slow_solve(self, n: int, m: int, pairs: List[Tuple[int, int]]) -> int:
        arr = [i for i in range(n + 1)]; pairs_set = set(pairs); ans = 0
        print(pairs_set)
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                segment = arr[i:j + 1]; valid = True
                for x in range(len(segment)):
                    if not valid: break
                    for y in range(x, len(segment)):
                        if (i + x, i + y) in pairs_set:
                            valid = False; break
 
                if valid: 
                    print(i, j)
                    ans += 1
 
        return ans
 
    def stress_test(self):
        n = 10; m = 2; all_pairs = []
        for i in range(1, 11):
            for j in range(i + 1, 11):
                all_pairs.append((i, j))
 
        
        # combs = itertools.combinations(all_pairs, m)
        # for c in combs:
        #     if self.fast_solve(n, m, list(c), )
        #     print(list(c))
 
        
 
        
 
 
 
solution_obj = Solution()
 
 
 
 
    