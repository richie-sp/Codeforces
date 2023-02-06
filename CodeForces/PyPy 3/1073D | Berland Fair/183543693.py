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
 
n, T = map(int, input().split())
a = list(map(int, input().split()))
 
# sum_a = sum(a)
# ans = n * (T // sum(a))
# T %= sum_a
 
 
candies = {i: None for i in range(len(a))}
 
ans = 0
while candies and T > 0:
    sum_a = 0
    to_delete = []
    for i in candies:
        if T >= a[i]:
            sum_a += a[i] 
        else:
            to_delete.append(i)
 
    for expensive_cand in to_delete:
        del candies[expensive_cand]
 
    if not candies: break
 
    if sum_a <= T:
        mult = T // sum_a
        T %= sum_a
        ans += mult * len(candies)
    else:
        for i in candies:
            if T >= a[i]:
                sum_a += a[i]
                T -= a[i]
                ans += 1
 
print(ans)
 