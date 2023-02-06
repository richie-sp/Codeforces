from sys import stdin
input = stdin.readline
 
for c in range(int(input())):
    n = int(input())
    s = input()[:-1]
 
    ans = 0
 
    for i in range(n):
        max_window = s[i:i+100]
        window_ctr = [0 for i in range(10)]
        found = set()
        maxim = 0
        for elem in max_window:
            if maxim > 10: break
 
            window_ctr[int(elem)] += 1; found.add(elem)
            maxim = max(maxim, window_ctr[int(elem)])
            
            if maxim <= len(found): ans += 1
 
    print(ans)