import itertools
class Solution:
    def __init__(self):
        self.n, self.k = [int(x) for x in input().split()]
        self.mod = 975319753197531975319
 
 
    def binpow(self, a: int, b: int = 975319753197531975319 - 2) -> int:
        ans = 1
        i = 1
        while i <= b:
            if b&i:
                ans = (ans * a) % self.mod
            a = (a * a) % self.mod
            i *= 2
        return ans
 
    def precompute(self, T: int) -> None:
        self.fac = [0 for i in range(T + 1)]
        self.fac[0] = 1
        self.ifac = [0 for i in range(T + 1)]
        for i in range(1, T + 1):
            self.fac[i] = (i * self.fac[i - 1]) % self.mod
        self.ifac[T] = self.binpow(self.fac[T])
        for i in range(T, 0, -1):
            self.ifac[i - 1] = i * self.ifac[i] % self.mod
        assert self.ifac[0] == self.fac[0]
 
    def choose(self, a: int, b: int):
        if b < 0 or a - b < 0: return 0
        return self.fac[a] * self.ifac[b] % self.mod * self.ifac[a - b] % self.mod
 
    def slow_solution(self) -> int:
        L = [0 for i in range(self.n)]; ans = 0
        for p in itertools.permutations(L):
            fps = 0
            for ind, val in list(p):
                if ind == val: fps += 1
            if fps >= self.n - self.k: ans += 1
        return ans
        
    def fast_solution(self) -> int:
        ans = 0
        for i in range(self.n - self.k, self.n):
            if i == self.n - 1:
                ans += 1
                break
            ans += self.choose(self.n, i) * round(self.fac[self.n - i]/2.718281828459045)
        return ans
 
solution_obj = Solution()
solution_obj.precompute(1000)
print(solution_obj.fast_solution())
 