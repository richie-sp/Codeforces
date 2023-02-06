n, k = [int(x) for x in input().split()]
s = input()
 
l, r = 0, 0
 
ans, num_b = 1, s[0] == 'b'
while l < len(s) and r < len(s):
    #window size = r - l + 1
    while num_b <= k:
        r += 1
        if r == len(s):
            break
 
        if s[r] == 'b': 
            num_b +=  1
 
        if num_b <= k:
            ans = max(ans, r - l + 1)
 
    #exit conditions: 1. num_b > k 2. r == len(s) ... 2nd one we can ignore
 
    if r == len(s):
        break
 
    while True:
        if s[l] == 'b':
            num_b -= 1
 
        l += 1
        if l == len(s):
            break
 
        if num_b == k:
            break
 
 
 
num_a = s[0] == 'a'
l, r = 0, 0
while l < len(s) and r < len(s):
    #window size = r - l + 1
    while num_a <= k:
        r += 1
        if r == len(s):
            break
 
        if s[r] == 'a': 
            num_a +=  1
 
        if num_a <= k:
            ans = max(ans, r - l + 1)
 
    #exit conditions: 1. num_a > k 2. r == len(s) ... 2nd one we can ignore
 
    if r == len(s):
        break
 
    while True:
        if s[l] == 'a':
            num_a -= 1
 
        l += 1
        if l == len(s):
            break
 
        if num_a == k:
            break
 
print(ans)
 
        
 
 
        
 