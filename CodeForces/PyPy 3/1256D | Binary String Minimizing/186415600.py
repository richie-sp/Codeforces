from sys import stdin
input = stdin.readline
 
"""
Idea: Count the number of 0s which fully move over to the beginning and the *remainder* for the left over 0 which represents how much the last zero moves over from its original position
"""
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = [int(ch) for ch in input()[:-1]]
    zero_inds_reversed = [i for i in range(len(s) - 1, -1, -1) if s[i] == 0]; zero_inds = zero_inds_reversed[::-1]
    
    inc = 0
    while zero_inds_reversed and k >= zero_inds_reversed[-1] - inc:
        k -= (zero_inds_reversed.pop(-1) - inc); inc += 1
 
    if not zero_inds_reversed:
        print(''.join(['0'] * len(zero_inds) + ['1'] * (n - len(zero_inds)))); continue
 
    ans = ['1'] * n
    for i in range(len(zero_inds) - len(zero_inds_reversed)):
        ans[i] = '0'
    ans[zero_inds_reversed[-1] - k] = '0'
    zero_inds_reversed.pop(-1)
    for i in zero_inds_reversed:
        ans[i] = '0'
    print(''.join(ans))
 
    