import datetime
 
r, s, p = [int(x) for x in input().split()]
memo = [[[None for p_ind in range(p + 1)] for s_ind in range(s + 1)] for r_ind in range(r + 1)]      
 
def compute_probs(r: int, s: int, p: int):
    if memo[r][s][p] is not None:
        return memo[r][s][p]
    
    if r == 0:
        return [0, 1, 0]
    if s == 0:
        return [0, 0, 1]
    if p == 0:
        return [1, 0, 0]
    if r == s == p:
        return [1/3, 1/3, 1/3]
 
    try:
        res = memo[s][p][r]
        if res is not None:
            x, y, z = res
            return [z, x, y]
    except:
        pass
 
    try:
        res = memo[p][r][s]
        if res is not None:
            x, y, z = res
            return [y, z, x]
    except:
        pass
 
    
 
    total = r*s + r*p + s*p
    r1_mult, r2_mult, r3_mult = r*s/total, r*p/total, s*p/total
 
    res1 = [r1_mult * elem for elem in compute_probs(r, s - 1, p)]
    res2 = [r2_mult * elem for elem in compute_probs(r - 1, s, p)]
    res3 = [r3_mult * elem for elem in compute_probs(r, s, p - 1)]
 
    ans = [x + y + z for x, y, z in zip(res1, res2, res3)]
    memo[r][s][p] = ans
 
    return ans
 
t1 = datetime.datetime.now()
x, y, z = compute_probs(r, s, p)
t2 = datetime.datetime.now()
 
 
print(f"{str(x)} {str(y)} {str(z)}")