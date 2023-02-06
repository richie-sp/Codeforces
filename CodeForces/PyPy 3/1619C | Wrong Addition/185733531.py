from sys import stdin
input = stdin.readline 
 
for _ in range(int(input())):
    a, s = map(str, input().split())
    ans = ''; curr = ''
    j = len(a) - 1
    for i in range(len(s) - 1, -1, -1):
        curr = s[i] + curr
        if j < 0:
            ans += str(int(s[i]))
        elif int(curr) >= int(a[j]):
            to_add = int(curr) - int(a[j])
            ans += str(to_add)
            # print(curr, 'hi', ans, j)
            j -= 1
            curr = ''
        else:
            continue
 
 
    res = ''
    ans = ans[::-1]
 
    max_len = max(len(ans), len(a))
    a = '0' * (max_len - len(a)) + a
    ans = '0' * (max_len - len(ans)) + ans
 
    for x, y in zip(ans, a):
        res += str(int(x) + int(y))
    
 
    if int(res) == int(s):
        print(int(ans))
    else:
        print(-1)
 
 
            