from sys import stdin
input = stdin.readline 
 
for c in range(int(input())):
    n, k = map(int, input().split())
    s = input()[:-1]
 
    possibilities_by_mod = [set() for i in range(k)]
    for i in range(len(s)):
        if s[i] != '?': possibilities_by_mod[i % k].add(s[i])
    
    ans = True
    for v in possibilities_by_mod:
        if len(v) > 1:
            ans = False
            break
 
    if not ans:
        print('NO')
        continue
 
    min_first = 0; max_first = 0
    for i in range(k):
        if len(possibilities_by_mod[i % k]) == 0:
            if s[i] == '1':
                min_first += 1; max_first += 1
            if s[i] == '?':
                max_first += 1
        else:
            for v in possibilities_by_mod[i % k]:
                break
            min_first += int(v); max_first += int(v)
 
    print('YES') if min_first <= k // 2 <= max_first else print('NO')
 
 
    