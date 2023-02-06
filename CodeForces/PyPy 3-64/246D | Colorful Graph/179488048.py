from sys import stdin
input = stdin.readline
 
n, m = map(int, input().split())
color = list(map(int, input().split()))
color_set = set(color)
 
cardinality = [set() for i in range(max(color) + 1)]
for l in range(m):
    u, v = map(int, input().split())
    if color[u - 1] != color[v - 1]: 
        cardinality[color[u - 1]].add(color[v - 1]) 
        cardinality[color[v - 1]].add(color[u - 1])
 
 
max_card, ans = -1, min(color)
for i in range(min(color), len(cardinality)):
    if i not in color_set: continue
    if len(cardinality[i]) > max_card: max_card = len(cardinality[i]); ans = i
 
print(ans)