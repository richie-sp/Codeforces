from sys import stdin
from collections import defaultdict, deque
from typing import Dict, List, Optional
import string, random
input = stdin.readline
 
 
def topo_sort(G: Dict[str, List[str]]) -> str:
    #first need indegrees
    indegree = {let: 0 for let in string.ascii_lowercase}; visited = {let: False for let in string.ascii_lowercase}
    for v in G.values():
        for ch in v: 
            indegree[ch] += 1
    
    bfs = deque()
    for letter, deg in indegree.items():
        if deg == 0: 
            bfs.append(letter)
            visited[letter] = True
 
 
    ordering = []; count = 0
    while bfs:
        curr_letter = bfs.popleft()
        ordering.append(curr_letter)
        for nex_letter in G[curr_letter]:
            indegree[nex_letter] -= 1
            if indegree[nex_letter] == 0 and not visited[nex_letter]: 
                bfs.append(nex_letter)
                visited[nex_letter] = True
 
        count += 1
 
 
    return '' if count != 26 else ''.join(ordering)
 
 
n = int(input()); G = {let: [] for let in string.ascii_lowercase}; names = []
for l in range(n): names.append(input()[:-1])
 
# names = []
# for i in range(1000):
#     name = []
#     for j in range(2000):
#         name.append(string.ascii_lowercase[random.randint(0, 25)])
#     names.append(''.join(name))
 
# names.sort()
 
 
 
if len(names) == 1:
    print(string.ascii_lowercase)
else:
    ans = string.ascii_lowercase
    for i in range(1, len(names)):
        prev_name = names[i - 1]; curr_name = names[i]
        prev_name += max(0, len(curr_name) - len(prev_name)) * ' '
        curr_name += max(0, len(prev_name) - len(curr_name)) * ' '
 
        
        for ch1, ch2 in zip(prev_name, curr_name):
            if ch2 == ' ' and ch1 != ' ':
                ans = ''; break
            if ch1 == ' ' or ch2 == ' ': break
            if ch1 == ch2: continue
            G[ch1].append(ch2)
            break
 
 
    if len(ans) == 0:
        print('Impossible')
    else:
        ans = topo_sort(G)
 
        if len(ans) != 26:
            print('Impossible')
        else:
            print(ans)
 
 
 
        