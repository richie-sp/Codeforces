from sys import stdin
input = stdin.readline
 
from collections import defaultdict
 
scores_by_name = defaultdict(int)
 
winner = None
info = []
for l in range(int(input())):
    name, sc = map(str, input().split())
    sc = int(sc)
    info.append([name, sc])
    scores_by_name[name] += sc
 
max_val = max(scores_by_name.values())
candidates = set([name for name in scores_by_name if scores_by_name[name] == max_val])
 
 
scores_by_name = defaultdict(int)
for name, sc in info:
    scores_by_name[name] += sc
    if name in candidates and scores_by_name[name] >= max_val:
        winner = name
        break
 
 
 
print(winner)
 
        
 
    