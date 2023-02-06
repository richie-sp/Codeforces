for case in range(int(input())):
    n = int(input())
    if n == 1:
        print(n) 
        continue
    else:
        ans = []
        ans.append(str(2))
        for i in range(3, n+1):
            ans.append(str(i))
        ans.append(str(1))
 
        print(' '.join(ans))