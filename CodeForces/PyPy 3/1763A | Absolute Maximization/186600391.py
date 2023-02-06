from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()));
    digits_by_ind = [set() for i in range(10)]
 
    max_len = float('-inf'); min_len = float('inf')
    for e in a:
        max_len = max(max_len, len(bin(e)[2:])); min_len = min(min_len, len(bin(e)[2:]))
        for ind, dig in enumerate(bin(e)[2:][::-1]):
            digits_by_ind[ind].add(int(dig))
 
    minim = 0; maxim = 0
    for ind, digits in enumerate(digits_by_ind):
        if ind <= min_len - 1:
            minim += 2 ** ind * min(digits)
        if ind <= max_len - 1:
            maxim += 2 ** ind * max(digits)
 
 
 
    print(maxim - minim)
 