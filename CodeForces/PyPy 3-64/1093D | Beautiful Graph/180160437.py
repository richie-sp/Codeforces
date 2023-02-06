from collections import defaultdict
from sys import stdin
input = stdin.readline
 
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
 
class Solution:
    @bootstrap
    def is_bipartite(self, v):
        for nei in self.G[v]:
            if not self.visited[nei]:
                self.visited[nei] = True
                self.color[nei] = abs(1 - self.color[v])
                
                res = yield self.is_bipartite(nei)
                if not res: yield False
 
            elif self.color[nei] == self.color[v]:
                yield False
        yield True
        
    def solve(self):
        for case in range(int(input())):
            G = defaultdict(list)
            n, m = map(int, input().split())
            for l in range(m):
                u, v = map(int, input().split())
                G[u].append(v); G[v].append(u)
            self.n = n; self.m = m; self.G = G; self.color = [0] * (n + 1); self.visited = [False] * (n + 1)
 
            visited = [False] * (n + 1); components = []
            ans = 1; mod = 998244353
            for i in range(1, n + 1):
                if visited[i]:
                    continue
 
                dfs = [i]
                component = set([i])
                while dfs:
                    curr = dfs.pop()
                    for nei in G[curr]:
                        if not visited[nei]:
                            visited[nei] = True
                            dfs.append(nei)
                            component.add(nei)
                if len(component) == 1:
                    ans = (ans * 3) % mod
                else:
                    components.append(component)
 
            for comp in components:
                for e in comp:
                    break
 
                if self.is_bipartite(e):
                    k = 0
                    for e in comp:
                        k += self.color[e]
                    l_ans = 1
                    for i in range(k):
                        l_ans = (l_ans * 2) % mod
 
                    r_ans = 1
                    for i in range(len(comp) - k):
                        r_ans = (r_ans * 2) % mod
                else:
                    l_ans = 0; r_ans = 0
 
                ans = (ans * (l_ans + r_ans)) % mod
                if ans == 0: break
 
            print(ans)
 
     
 
solution_obj = Solution()
solution_obj.solve()