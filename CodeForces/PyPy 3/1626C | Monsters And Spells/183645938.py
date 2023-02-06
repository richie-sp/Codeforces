for case in range(int(input())):
    n = int(input())
    k = list(map(int, input().split()))
    h = list(map(int, input().split()))
 
    #lb[i]: minimum value required at point i (lower bound) 
    lb = [0] * n
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            maxim = h[i]; lb[i] = maxim
        else:
            prev_lb = lb[i + 1] - (k[i + 1] - k[i]); maxim = max(h[i], prev_lb); lb[i] = maxim
 
 
    ans = 0
    for i in range(n):
        if i == 0:
            ans += (lb[i] * (lb[i] + 1) // 2); continue
 
        #if y distance between lower bounds less than or equals x distance, we can optionally just keep moving forward ...store option as option 1 
        x_diff = k[i] - k[i - 1]; option1, option2 = float('inf'), float('inf')
        if lb[i] - lb[i - 1] <= x_diff:
            target = lb[i - 1] + x_diff
            option1 = target * (target + 1) // 2 - lb[i - 1] * (lb[i - 1] + 1) // 2
 
        #option2 is only valid if x_diff >= lb[i]
        if x_diff >= lb[i]:
            option2 = lb[i] * (lb[i] + 1) // 2
 
        if option1 < option2:
            lb[i] = target
 
        ans += min(option1, option2)
 
    print(ans)
 
 
            
 
 
        
 
        
 
 