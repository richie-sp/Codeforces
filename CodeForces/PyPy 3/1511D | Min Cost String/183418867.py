from sys import stdin
from collections import defaultdict
import string
input = stdin.readline
 
class Solution:
    def dfs(self, u):
        while self.G[u]:
            v = self.G[u].pop()
            self.dfs(v)
        self.tour.append(u)
 
    def find_tour(self):
        self.n, self.k = map(int, input().split())
        letters = string.ascii_lowercase[:self.k]; self.tour = []
 
        self.G = defaultdict(list)
        for l1 in letters:
            for l2 in letters:
                self.G[l1].append(l2)
 
        self.dfs('a')
        self.tour.pop()
 
        ans = []
        for i in range(self.n):
            ans.append(self.tour[i % len(self.tour)])
 
        print(''.join(ans))
 
 
solution_obj = Solution()
solution_obj.find_tour()
 
 
        
 
#we know it's euler so no need to check 
 
 
 
 
 