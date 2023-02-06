from sys import stdin
input = stdin.readline
 
factorial = [1, 1]; prime = 10 ** 9 + 7
for i in range(2, 101):
    factorial.append((factorial[-1] * i) % prime)
 
def inv(a, n):
    if(a == 1):
        return 1
    return int((1 - inv(n % a, a) * n) / a + n)
 
def comb(n, k):
    if k < 0 or k > n: return 0
    return (factorial[n] * inv(factorial[k], prime) * inv(factorial[n - k], prime)) % prime
 
for _ in range(int(input())):
    n, i, j, x, y = map(int, input().split())
    if (j == y == n) or (i == 1 and x == n):
        print(0); continue
    if x < y: x, y, i, j = y, x, n - j + 1, n - i + 1
 
    if x == n:
        ans = (comb((x - 1) - (y + 1) + 1, (j - 1) - (i + 1) + 1) * comb(y - 1, n - (j + 1) + 1)) % prime
    else:
        ans = 0; l = (y - 1) - (n - (j + 1) + 1)
        for k in range(i + 1, j):
            ans += comb(y - 1, n - (j + 1) + 1) * comb((x - 1) - (y + 1) + 1, (i - 1) - (l + 1) + 1) * comb((n - 1) - (x + 1) + 1, (k - 1) - (i + 1) + 1); ans %= prime
 
        for k in range(2, i):
            ans += comb(y - 1, n - (j + 1) + 1) * comb((x - 1) - (y + 1) + 1, (j - 1) - (i + 1) + 1) * comb((n - 1) - (x + 1) + 1, (i - 1) - (k + 1) + 1); ans %= prime
 
    print(ans)
 
 
 
    