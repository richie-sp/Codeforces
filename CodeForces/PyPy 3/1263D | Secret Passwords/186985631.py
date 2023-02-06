from sys import stdin 
from collections import defaultdict
input = stdin.readline
 
 
class Solution:
    def __init__(self):
        self.passwords = []
        for line in range(int(input())):
            self.passwords.append(input()[:-1])
 
        self.G = defaultdict(set); self.letters = set()
        for password in self.passwords:
            for ch in password:
                self.G[ch].add(password)
                self.G[password].add(ch)
                self.letters.add(ch)
 
        self.all_visited = set(); self.curr_visited = set(); ans = 0
        for letter in self.letters:
            if letter in self.all_visited: continue
            self.curr_visited = set([letter])
            self.dfs(letter)
            for k in self.curr_visited: self.all_visited.add(k)
            ans += 1    
 
        print(ans)
 
    def dfs(self, node):
        for nex in self.G[node]:
            if nex not in self.curr_visited:
                self.curr_visited.add(nex)
                self.dfs(nex)
 
solution_obj = Solution()
 
 
 
 
 
 