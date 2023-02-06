def f(s: str, c: str) -> int:
    n = len(s)
    if n == 1: 
        return 0 if s[0] == c else 1
 
    opt1 = n // 2 - s[:n // 2].count(c) + f(s[n // 2:], chr(ord(c) + 1))
    opt2 = n // 2 - s[n // 2:].count(c) + f(s[:n // 2], chr(ord(c) + 1))
 
    return min(opt1, opt2)
 
for c in range(int(input())):
    n = int(input())
    s = input()
    print(f(s, 'a'))
 
 
 
 
 
 
 
 
 
    
 
 
    