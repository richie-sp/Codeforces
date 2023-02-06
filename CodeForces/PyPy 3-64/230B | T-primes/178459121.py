 
 
 
n = 10 ** 6
primes = [0, 0] + [1] * (n - 1)
i = 2
while i * i < n + 1:
    if primes[i]:
        primes[i * i:n + 1:i] = [0] * ((n + 1 - i * i - 1) // i + 1)
    i += 1 if i == 2 else 2 # skip even numbers
 
primes_set = set([ind ** 2 for ind, val in enumerate(primes) if val])
 
n = int(input())
 
nums = [int(x) for x in input().split()]
for x in nums:
    print('YES') if x in primes_set else print('NO')
 
 
 
 
 
 