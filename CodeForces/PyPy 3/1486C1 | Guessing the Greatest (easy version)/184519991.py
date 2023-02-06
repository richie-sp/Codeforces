from sys import stdout
 
n = int(input())
l, r, i = 1, n, None
 
for i in range(100):
    if r - l == 1:
        print(f"? {l} {r}")
        stdout.flush()
        i = int(input())
        if i == l:
            print(f"! {r}")
        else:
            print(f"! {l}")
        break
    elif l == r:
        print(f"! {l}")
        break
        
    print(f"? {l} {r}")
    stdout.flush()
    i = int(input())
    mid = (l + r) // 2
    if i <= mid:
        print(f"? {l} {mid}")
        stdout.flush()
        j = int(input())
 
        if i != j:
            l, r = mid + 1, r
        else:
            l, r = l, mid
    else:
        print(f"? {mid} {r}")
        stdout.flush()
        j = int(input())
 
        if i != j:
            l, r = l, mid - 1
        else:
            l, r = mid, r
            
 
 
 
 
            