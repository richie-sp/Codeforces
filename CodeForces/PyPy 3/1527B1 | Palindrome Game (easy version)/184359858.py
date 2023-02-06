from sys import stdin
input = stdin.readline 
 
for c in range(int(input())):
    n = int(input())
    s = [int(e) for e in input()[:-1]]; s_ct = s.count(0)
    if s_ct % 2 == 0:
        print('BOB'); continue
 
    if s_ct == 1:
        print('BOB'); continue
 
    print('ALICE')
 
    