for case in range(int(input())):
    n, m = [int(x) for x in input().split()]
    
    if n == 1 and m == 1:
        print(0)
        continue
        
    print((n-1) + (m-1) + min(m, n))