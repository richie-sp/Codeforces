from sys import stdin 
input = stdin.readline 
 
t = int(input())
for case in range(t):
    n0, n1, n2 = map(int, input().split())
 
    if [n0, n1] == [0, 0]:
        ans = ['1'] * (n2 + 1)
        print(''.join(ans)); continue 
 
    if n1 % 2 == 1:
        ans = ['0'] * (n0 + 1)
        for switch in range(n1):
            if switch % 2 == 0:
                ans.append('1')
            else:
                ans.append('0')
        ans += ['1'] * n2
        print(''.join(ans))
 
    else:
        ans = ['0'] * (n0 + 1)
        for switch in range(n1):
            if switch % 2 == 0:
                if switch == 0:
                    ans += ['1'] * (n2 + 1)
                else:
                    ans.append('1')
            else:
                ans.append('0')
        
        print(''.join(ans))