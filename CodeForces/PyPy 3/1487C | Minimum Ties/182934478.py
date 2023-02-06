for c in range(int(input())):
    n = int(input())
    outdeg = [0 for i in range(n + 1)]; points = [0 for i in range(n + 1)]; color = [0 for i in range(n + 1)]
    
    ans = []; wins = 0; max_wins = n * (n - 1) // 2 - (n * (n - 1) // 2) % n; max_out = max_wins // n
    
 
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if outdeg[i] < max_out:
                outdeg[i] += 1; ans.append('1'); points[i] += 3
            elif max_wins != n * (n - 1) // 2 and color[i] == color[j] == 0:
                color[i] = 1; color[j] = 1; ans.append('0'); points[i] += 1; points[j] += 1
            else:
                outdeg[j] += 1; ans.append('-1'); points[j] += 3
 
 
    print(' '.join(ans))