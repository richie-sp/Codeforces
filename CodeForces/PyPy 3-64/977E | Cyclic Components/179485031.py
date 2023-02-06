import sys
from collections import defaultdict 
 
input = sys.stdin.readline
 
 
class Solution:
    def __init__(self):
        degree, G = defaultdict(int), defaultdict(list)
 
        n, m = map(int, input().split())
        for l in range(m):
            u, v = map(int, input().split())
            degree[u] += 1; degree[v] += 1; G[u].append(v); G[v].append(u)
 
        self.n, self.m, self.G, self.degree = n, m, G, degree
 
    def solve(self):
        self.all_visited = set()
        components = []
        for node in range(1, self.n + 1):
            if node in self.all_visited: continue
            self.curr_visited = set([node])
            # self.dfs(node)
            dfs = [node]
            while dfs:
                curr_node = dfs.pop()
                for nex in self.G[curr_node]:
                    if nex not in self.curr_visited:
                        self.curr_visited.add(nex)
                        dfs.append(nex)
 
            for n in self.curr_visited: self.all_visited.add(n)
            components.append(self.curr_visited)
 
        ans = 0
        for comp in components:
            if len(comp) <= 2:
                continue
            valid = True
            for e in comp:
                if self.degree[e] != 2: 
                    valid = False
                    break
 
            if valid: ans += 1
 
        print(ans)
 
 
solution_obj = Solution()
solution_obj.solve()
 