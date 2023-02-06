s = input()
a_inds, b_inds = [], []
 
for i in range(len(s) - 1):
    if s[i:i+2] == 'AB':
        a_inds.append(i)
    elif s[i:i+2] == 'BA':
        b_inds.append(i)
 
 
 
found = False
for i in a_inds:
    if len(b_inds) == 0: break
 
    if abs(b_inds[0] - i) >= 2 or abs(b_inds[-1] - i) >= 2:
        found = True
        break
    
 
print('YES') if found else print('NO')
    
 
 
 
 
 