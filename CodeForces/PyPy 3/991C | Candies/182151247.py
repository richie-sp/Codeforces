def is_possible(m: int, k: int) -> bool:
    #minim = minimum candies vasya needs to take
    if m % 2 == 0:
        minim = m // 2
    else:
        minim = m // 2 + 1
 
    turn = 'vasya'; v_count = 0
    while m > 0:
        if turn == 'vasya':
            rem = min(k, m)
            v_count += rem
            m -= rem
            turn = 'petya'
        elif turn == 'petya':
            turn = 'vasya'
            rem = m // 10
            m -= rem
 
    return v_count >= minim
 
 
    
 
n = int(input())
l = 1; r = n
 
 
while l < r:
    if l == r - 1: break
    m = (l + r) // 2
    if is_possible(n, m):
        r = m
    else:
        l = m
 
 
if is_possible(n, l + 1): ans = l + 1
if is_possible(n, l): ans = l
 
print(ans)