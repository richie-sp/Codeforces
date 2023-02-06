from sys import stdin
from collections import defaultdict, deque
input = stdin.readline
 
n = int(input())
G = defaultdict(list)
for l in range(n - 1):
    u, v = map(int, input().split())
    G[u].append(v); G[v].append(u)
 
a = deque(map(int, input().split()))
level_by_node = {}
visited = [False] * (n + 1)
visited[1] = True
bfs = deque([(1, 0)])
 
while bfs:
    curr_node, curr_level = bfs.popleft()
    level_by_node[curr_node] = curr_level
 
    for nex in G[curr_node]:
        if not visited[nex]:
            bfs.append((nex, curr_level + 1))
            visited[nex] = True
ans = True
for i in range(1, len(a)):
    prev = a[i - 1]; curr = a[i]
    if level_by_node[prev] > level_by_node[curr]:
        ans = False
        break
 
if ans:
    to_process = deque()
    visited = [False] * (n + 1)
    while a:
        # print(to_process)
        head = a.popleft()
        visited[head] = True
        to_process.append([head, {e for e in G[head] if not visited[e]}])
        if len(a) == n - 1:
            continue
 
        if head not in to_process[0][1]:
            ans = False
            break
 
        to_process[0][1].remove(head)
        while to_process and len(to_process[0][1]) == 0: to_process.popleft()
 
 
print('yEs') if ans else print('nO')
 
 
 
 
 