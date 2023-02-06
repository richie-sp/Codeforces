from sys import stdin
input=stdin.readline
 
from collections import defaultdict, Counter
 
class Solution:
    def dfs(self, u: int):
        for v in self.G[u]:
            if v not in self.curr_visited:
                self.curr_visited.add(v)
                self.dfs(v)
 
 
    def solve(self):
        for case in range(int(input())):
            n, k = map(int, input().split())
            s = input()
 
            G = defaultdict(set)
            for i in range(n):
                ptr1, ptr2 = i, n - 1 - i
 
                G[ptr1].add(ptr2)
                G[ptr2].add(ptr1)
 
            for mod in range(k):
                for x in range(mod, n, k):
                    G[mod].add(x)
                    G[x].add(mod)
 
            self.G = G
 
            self.all_visited = set()
            self.curr_visited = set()
            self.groups = []
            for i in range(n):
                if i not in self.all_visited:
                    self.curr_visited = set([i])
                    self.dfs(i)
                
                for e in self.curr_visited: self.all_visited.add(e)
 
                if len(self.curr_visited) > 0:
                    self.groups.append(self.curr_visited)
 
                self.curr_visited = set()
 
            ans = 0
            for group in self.groups:
                l_ctr = Counter()
                for ind in group:
                    l_ctr[s[ind]] += 1
 
                ans += (len(group) - l_ctr.most_common(1)[0][1])
 
            print(ans)
 
 
 
solution_obj = Solution()
solution_obj.solve()
 
    
 
    
 
 
 