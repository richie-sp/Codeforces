import os
import sys
from io import BytesIO, IOBase
 
_str = str
str = lambda x=b"": x if type(x) is bytes else _str(x).encode()
 
BUFSIZE = 8192
 
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
output = lambda x: sys.stdout.write(x)
 
for case in range(int(input())):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
 
    #returns the value which makes x as close to s as possible
    def closex(i) -> int:
        if a[i] >= s:
            return s
        return a[i]
 
    def closey(i) -> int:
        return a[i] - closex(i)
 
    dp = [[float('inf'), float('inf')] for i in range(n)]
    dp[1][0] = a[0] * closex(1); dp[1][1] = a[0] * closey(1)
 
    for i in range(2, n - 1):
        dp[i][0] = min(dp[i - 1][0] + (a[i - 1] - min(a[i - 1], s)) * min(a[i], s), dp[i - 1][1] + min(a[i - 1], s) * min(a[i], s))
        dp[i][1] = min(dp[i - 1][0] + (a[i - 1] - min(a[i - 1], s)) * (a[i] - min(a[i], s)), dp[i - 1][1] + min(a[i - 1], s) * (a[i] - min(a[i], s)))
 
    ans = min(dp[n - 2][0] + closey(n - 2) * a[n - 1], dp[n - 2][1] + closex(n - 2) * a[n - 1])
 
    print(ans)