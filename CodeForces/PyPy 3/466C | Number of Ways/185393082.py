import os
import sys
import bisect
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
 
n = int(input())
a = list(map(int, input().split()))
 
if len(a) < 3:
    print(0)
elif sum(a) % 3 != 0:
    print(0)
else:
    targ = sum(a) // 3
    if targ == 0:
        #you can't use point at end as cutoff
        i_inds = []; curr_sum = 0
        for i in range(n - 1):
            curr_sum += a[i]
            if curr_sum == 0:
                i_inds.append(i)
 
        k = len(i_inds)
        print(k * (k - 1) // 2)
    else:
        t_1 = targ; t_2 = targ * 2; curr_sum = 0; i_inds = []; j_inds = []
        for i in range(n - 1):
            curr_sum += a[i]
            if curr_sum == t_1:
                i_inds.append(i)
            if curr_sum == t_2:
                j_inds.append(i)
        ans = 0
        for e in i_inds:
            ind = bisect.bisect_right(j_inds, e)
            ans += len(j_inds) - ind
 
        print(ans)
 