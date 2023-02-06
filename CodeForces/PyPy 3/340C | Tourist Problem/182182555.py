from sys import stdin
from fractions import Fraction
import itertools
import math
input = stdin.readline
 
class Solution:
    def __init__(self):
        self.n = int(input())
        self.a = list(map(int, input().split()))
        self.a.sort()
 
    def slow_solve(self) -> float:
        ans = 0; total_dist = 0
        for perm in itertools.permutations(self.a):
            prev = 0
            for elem in list(perm):
                total_dist += abs(elem - prev)
                prev = elem
 
        return total_dist / math.factorial(self.n)
 
    def faster_solve(self) -> float:
        E_pairwise_dist = 0
        for i in range(len(self.a)):
            for j in range(i + 1, len(self.a)):
                E_pairwise_dist += abs(self.a[j] - self.a[i])
 
        E_pairwise_dist = Fraction(E_pairwise_dist, (self.n * (self.n - 1) // 2))
 
        
        return (self.n - 1) * E_pairwise_dist + Fraction(sum(self.a), len(self.a))
 
    def official_solve(self) -> float:
        base_sum = 0; E_pairwise_dist = 0
        for i in range(1, len(self.a)):
            base_sum += self.a[i] - self.a[0]
 
        E_pairwise_dist += base_sum
        i = 1
        for k in range(self.n - 1, 0, -1):
            base_sum -= k * (self.a[i] - self.a[i - 1])
            E_pairwise_dist += base_sum
            i += 1
 
        E_pairwise_dist = Fraction(E_pairwise_dist, (self.n * (self.n - 1) // 2))
 
        return (self.n - 1) * E_pairwise_dist + Fraction(sum(self.a), len(self.a))
 
        
 
 
 
 
 
solution_obj = Solution()
ans = solution_obj.official_solve()
print(' '.join([str(e) for e in [ans.numerator, ans.denominator]]))
                
 
 