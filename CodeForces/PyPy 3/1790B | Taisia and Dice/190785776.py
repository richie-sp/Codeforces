from sys import stdin
input = stdin.readline
 
for case in range(int(input())):
    n, s, r = map(int, input().split())
    final = s - r
    a = r // (n - 1); b = a + 1
    b_ct = r % (n - 1); a_ct = n - 1 - b_ct
 
    ans = [str(a)] * a_ct + [str(b)] * b_ct + [str(final)]
    print(' '.join(ans))