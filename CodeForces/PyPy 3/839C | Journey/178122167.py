from collections import defaultdict, deque
from typing import List, Dict 
 
'''
DFS optimization: 
 
https://www.python.org/doc/essays/graphs/
 
'''
 
 
n = int(input())
if n == 1:
    print(0)
elif n == 2:
    u, v = [int(x) for x in input().split()]
    print(1)
else:
    adj = defaultdict(list)
 
    for edge in range(n - 1):
        u, v = [int(x) for x in input().split()]
        adj[u].append(v)
        adj[v].append(u)
    
    #curr_node, curr_prob, curr_level
    bfs, visited, ans = deque([(1, 1, 0)]), set([1]), 0
 
    while bfs:
        curr_node, curr_prob, curr_level = bfs.popleft()
        
        num_adj = 0
        for nex_node in adj[curr_node]:
            if nex_node not in visited: num_adj += 1
 
        for nex_node in adj[curr_node]:
            if nex_node not in visited:
                visited.add(nex_node)
                bfs.append((nex_node, curr_prob / num_adj, curr_level + 1))
 
        if num_adj == 0:
            ans += curr_prob * curr_level
 
    print(ans)
 
 
 
 
    
 
    
 