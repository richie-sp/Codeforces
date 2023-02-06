from sys import stdin
from collections import Counter
input = stdin.readline
 
def get_prime_factorization(n: int):
    factorization = []
    d = 2
    while d ** 2 <= n:
        while n % d == 0:
            factorization.append(d); n //= d
        d += 1
 
    if n > 1:
        factorization.append(n)
    return factorization
 
for case in range(int(input())):
    n = int(input())
    factorization = Counter(get_prime_factorization(n))
 
    info = []; prod = 1
    for k, v in factorization.items():
        info.append((v, k)); prod *= k
 
    info.sort()
 
    ans = 0
    for i in range(len(info)):
        if i == 0:
            ans += prod * info[i][0]
        else:
            prod //= info[i - 1][1]
            ans += prod * (info[i][0] - info[i - 1][0])
    
    print(ans)
    