import math 
 
n, m = map(int, input().split())
 
print(math.comb(2*m + n - 1, n - 1) % (10 ** 9 + 7))
 