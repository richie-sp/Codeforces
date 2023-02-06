from collections import deque
 
n, m = [int(x) for x in input().split()]
 
bfs = deque([(n, 0)])
 
visited = set()
ans = None
its = 0
while bfs:
    its += 1
    curr_num, curr_steps = bfs.popleft()
 
    if curr_num == m:
        ans = curr_steps
        break
    if curr_num < 10 ** 6:
        if curr_num >= 0:
            if curr_num - 1 not in visited:
                bfs.append((curr_num - 1, curr_steps + 1))
                visited.add(curr_num - 1)
 
        if curr_num * 2 not in visited:
            bfs.append((curr_num * 2, curr_steps + 1))
            visited.add(curr_num * 2)
 
print(ans)