from sys import stdin
input = stdin.readline
import math
 
def get_factors(x: int):
    if x == 0: return []
    factors = []
    for i in range(1, int(math.ceil(x ** 0.5) + 1)):
        if x % i == 0:
            if i == x // i:
                factors.append(i)
            else:
                factors.append(i); factors.append(x // i)
    return list(set(factors))
 
factors_map = [get_factors(x) for x in range(10 ** 5 + 1)]
 
for case in range(int(input())):
    n, m = map(int, input().split());
    a = list(map(int, input().split())); a.sort()
    factors = set()
    for f in factors_map[a[0]]:
        if f <= m: factors.add(f)
 
    count_by_mod = [0 for i in range(m + 1)]; ans = float('inf'); r = 0
    for f in factors: 
        if f <= m: count_by_mod[f] += 1
    found = False
    for l in range(len(a)):
        if len(factors) == m: found = True
        while len(factors) < m:
            r += 1 
            if r == len(a): break
            for f in factors_map[a[r]]:
                if f <= m: 
                    count_by_mod[f] += 1
                    factors.add(f)
        if len(factors) == m: found = True
        #postcondition: len(factors_map) = m
        try:
            if r >= l:
                ans = min(ans, a[r] - a[l])
        except: break
        # print(count_by_mod, factors, r, l)
        for f in factors_map[a[l]]:
            if f <= m: count_by_mod[f] -= 1
            if f <= m and count_by_mod[f] == 0:
                factors.discard(f)
 
    print(ans) if (ans < float('inf') and found) else print(-1)
 
 
    