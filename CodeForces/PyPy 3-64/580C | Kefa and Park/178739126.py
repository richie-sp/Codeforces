from collections import defaultdict, deque
 
n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
 
G = defaultdict(list)
for line in range(n - 1):
    x, y = [int(x) for x in input().split()]
    G[x - 1].append(y - 1)
    G[y - 1].append(x - 1)
 
bfs = deque([(0, a[0])])
visited = set([0])
ans = 0
while bfs:
    curr, cats = bfs.popleft()
    
    adj_count = 0
    for nex in G[curr]:
        if nex not in visited:
            adj_count += 1
 
    if adj_count == 0:
        ans += 1
 
    for nex in G[curr]:
        if nex not in visited:
            if a[nex] == 0:
                visited.add(nex)
                bfs.append((nex, 0))
            elif cats + 1 <= m:
                visited.add(nex)
                bfs.append((nex, cats + 1))
        
 
 
 
print(ans)
 