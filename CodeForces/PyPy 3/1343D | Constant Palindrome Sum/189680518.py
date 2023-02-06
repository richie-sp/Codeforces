from sys import stdin
from itertools import accumulate
input = stdin.readline
 
for case in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
 
    #have zero ops and 1 ops, can calculate 2 ops
    zero_op_count = [0 for i in range(2*k + 2)]; psum_one_op = [0 for i in range(2*k + 2)]
    for i in range(n // 2):
        x = a[i]; y = a[n - 1 - i]
        zero_op_count[x + y] += 1
        minim_one = min(x, y) + 1; maxim_one = max(x, y) + k
        psum_one_op[minim_one] += 1; psum_one_op[maxim_one + 1] -= 1
        psum_one_op[x + y] -= 1; psum_one_op[x + y + 1] += 1
 
    psum_one_op = list(accumulate(psum_one_op))
    ans = float('inf')
    for ind, one_ops in enumerate(psum_one_op):
        two_ops = n // 2 - one_ops - zero_op_count[ind]
        ops = two_ops * 2 + one_ops
        # print(ind, ops, two_ops, one_ops)
        ans = min(ans, ops)
 
    print(ans)
 
    