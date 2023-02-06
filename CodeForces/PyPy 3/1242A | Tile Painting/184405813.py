"""
vector<long long> trial_division1(long long n) {
    vector<long long> factorization;
    for (long long d = 2; d * d <= n; d++) {
        while (n % d == 0) {
            factorization.push_back(d);
            n /= d;
        }
    }
    if (n > 1)
        factorization.push_back(n);
    return factorization;
}
"""
from typing import List
def get_prime_factorization(n: int) -> List[int]:
    factorization = []
    d = 2
    while d ** 2 <= n:
        while n % d == 0:
            factorization.append(d); n //= d
        d += 1
 
    if n > 1:
        factorization.append(n)
    return factorization
 
 
n = int(input())
factorization_set = set(get_prime_factorization(n))
if len(factorization_set) == 0:
    print(1)
elif len(factorization_set) > 1:
    print(1)
else:
    print(min(factorization_set))
 