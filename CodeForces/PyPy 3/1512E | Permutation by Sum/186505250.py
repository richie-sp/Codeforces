from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    n, l, r, s = map(int, input().split()); l -= 1; r -= 1
    k = r - l + 1; avg = s / k; kc = n - k
 
    min_s = k * (k + 1) // 2; max_s = n * (n + 1) // 2 - kc * (kc + 1) // 2
    if not (min_s <= s <= max_s):
        print(-1); continue
 
    if k % 2 == 1:
        q = (k - 1) // 2; segment = [i for i in range(int(avg) - q, int(avg) + q + 2)]
    else:
        if abs(int(avg) - avg) < 10 ** (-8):
            q = k // 2; segment = [i for i in range(int(avg - q), int(avg + q) + 2) if i != int(avg)]
        else:
            q = k // 2 - 0.5; segment = [i for i in range(int(avg - q), int(avg + q) + 2)]
    curr_sum = sum(segment); bad = curr_sum - s; segment = [e for e in segment if e != bad]
 
 
 
    if sum(segment) != s:
        print(f"Wrong segment sum: n {n} l {l} r {r} s {s} segment {segment}")
 
    elems = set(i for i in range(1, n + 1))
    for elem in segment: elems.remove(elem)
    ans = [0 for i in range(n)]; seg_ptr = 0
    for i in range(n):
        if not (l <= i <= r):
            ans[i] = elems.pop()
        else:
            ans[i] = segment[seg_ptr]; seg_ptr += 1
 
    print(' '.join(str(ch) for ch in ans))
 
 
        