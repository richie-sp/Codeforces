from sys import stdin
input = stdin.readline
 
prod_info = []; ans = 0; discount = 0
for c in range(int(input())):
    ai, bi = map(int, input().split())
    prod_info.append((bi, ai)); ans += 2 * ai
 
ptr = ans // 2
 
prod_info.sort(reverse = True)
 
for bi, ai in prod_info:
    if ptr - bi <= 0: continue 
    red = min(ptr - bi, ai); discount += red; ptr -= red
 
print(ans - discount)