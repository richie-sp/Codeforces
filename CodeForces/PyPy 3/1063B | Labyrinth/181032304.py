# import os,sys
# from io import BytesIO, IOBase
# from collections import deque
 
# def main():
#     n,m = map(int,input().split())
#     r,c = map(int, input().split())
#     l_max,r_max = map(int,input().split())
 
#     grid = []
#     for i in range(n):
#         grid.append(list(input()))
 
#     grid[r - 1][c - 1] = '+'; ans = 1
#     bfs = deque([((r - 1, c - 1), l_max, r_max)])
 
#     drs = [0, 0, 1, -1]; dcs = [-1, 1, 0, 0]; plus = '+'; star = '*'
#     while bfs:
#         curr_loc, l_rem, r_rem = bfs.popleft()
#         i, j = curr_loc
        
#         for dr, dc in zip(drs, dcs):
#             u, v = i + dr, j + dc
#             if not (0 <= u < n): continue
#             if not (0 <= v < m): continue
#             if not (grid[u][v] != plus and grid[u][v] != star): continue
 
#             if dc == -1:
#                 if l_rem > 0:
#                     grid[u][v] = '+'; ans += 1
#                     bfs.append(((u, v), l_rem - 1, r_rem))
#                 else:
#                     continue
#             elif dc == 1:
#                 if r_rem > 0:
#                     grid[u][v] = '+'; ans += 1
#                     bfs.append(((u, v), l_rem, r_rem - 1))
#                 else:
#                     continue
#             else:
#                 grid[u][v] = '+'; ans += 1
#                 bfs.appendleft(((u, v), l_rem, r_rem)) 
 
#     print(ans)
 
 
 
# # Fast IO Region
# BUFSIZE = 8192
# class FastIO(IOBase):
#     newlines = 0
#     def __init__(self, file):
#         self._fd = file.fileno()
#         self.buffer = BytesIO()
#         self.writable = "x" in file.mode or "r" not in file.mode
#         self.write = self.buffer.write if self.writable else None
#     def read(self):
#         while True:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             if not b:
#                 break
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines = 0
#         return self.buffer.read()
#     def readline(self):
#         while self.newlines == 0:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             self.newlines = b.count(b"\n") + (not b)
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines -= 1
#         return self.buffer.readline()
#     def flush(self):
#         if self.writable:
#             os.write(self._fd, self.buffer.getvalue())
#             self.buffer.truncate(0), self.buffer.seek(0)
# class IOWrapper(IOBase):
#     def __init__(self, file):
#         self.buffer = FastIO(file)
#         self.flush = self.buffer.flush
#         self.writable = self.buffer.writable
#         self.write = lambda s: self.buffer.write(s.encode("ascii"))
#         self.read = lambda: self.buffer.read().decode("ascii")
#         self.readline = lambda: self.buffer.readline().decode("ascii")
# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
# input = lambda: sys.stdin.readline().rstrip("\r\n")
# if __name__ == "__main__":
#     main()
 
 
"""
Not my code
"""
 
from collections import deque
 
n,m=map(int,input().split())
r,c=map(int,input().split())
x,y=map(int,input().split())
 
l=[]
for i in range(n):
    l.append(list(input()))
v=[[0]*m for i in range(n)]
#print(v)
q=deque()
q.append([r-1,c-1,x,y])
c=0
while len(q)!=0:
    t=q.popleft()
    tx=t[0]
    ty=t[1]
    tl=t[2]
    tr=t[3]
    #print(tx+1,ty+1)
    if v[tx][ty]==1 or l[tx][ty]!='.':
        continue
    c+=1
    v[tx][ty]=1
    if tx+1<n:
        q.appendleft([tx+1,ty,tl,tr])
    if tx-1>=0:
        q.appendleft([tx-1,ty,tl,tr])
    if tl>0 and ty-1>=0:
        q.append([tx,ty-1,tl-1,tr])
    if tr>0 and ty+1<m:
        q.append([tx,ty+1,tl,tr-1])
print(c)