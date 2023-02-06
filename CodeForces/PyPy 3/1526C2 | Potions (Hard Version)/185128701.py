import heapq
from sys import stdin
input = stdin.readline 
 
n = int(input())
a = list(map(int, input().split())); health = 0; negatives = []; potions = 0
 
for ind, elem in enumerate(a):
    if elem >= 0:
        health += elem; potions += 1; continue 
 
    if health + elem >= 0:
        heapq.heappush(negatives, elem); potions += 1; health += elem; continue
 
    #health + elem < 0... if length of negatives used prior is 0, just skip current one
    if not negatives: continue
    if elem > negatives[0]:
        old = heapq.heappop(negatives); heapq.heappush(negatives, elem); health += (elem - old)
 
 
print(potions)
 
 
    