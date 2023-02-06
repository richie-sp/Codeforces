from collections import Counter
 
for case in range(int(input())):
    s = input()
 
    ans = len(s) - 2
    if ans == 0:
        print(0)
        continue
 
    s_ctr = Counter(s)
    for v in s_ctr.values():
        ans = min(ans, len(s) - v)
    
    for d1 in range(10):
        for d2 in range(10):
            if d1 == d2: continue
 
 
            curr_size = 0
            search = str(d1)
            for elem in s:
                if elem == search == str(d1):
                    curr_size += 1
                    search = str(d2)
                elif elem == search == str(d2):
                    curr_size += 1
                    search = str(d1)
 
            ans = min(ans, len(s) - (curr_size - curr_size % 2))
            
    
    print(ans)
 
 
 
 
    
 
    