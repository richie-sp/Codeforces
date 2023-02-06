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
    def __init__(self):
        G = defaultdict(list)
        n, m = map(int, input().split())
        self.edges = []
        for l in range(m):
            u, v = map(int, input().split())
            G[u].append(v)
            G[v].append(u)
            self.edges.append([u, v])
        self.n = n; self.m = m; self.G = G; self.color = [0] * (n + 1); self.visited = [False] * (n + 1)
    
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
 
    def gen_ans(self) -> str:
        mp = {(0, 1): '1', (1, 0): '0'}
        return ''.join([mp[(self.color[u], self.color[v])] for u, v in self.edges if (self.color[u], self.color[v]) in mp])
 
 
solution_obj = Solution()
if solution_obj.is_bipartite(1):
    print('yEs')
    print(solution_obj.gen_ans())
else:
    print('nO')
 
 
 
 