import bisect
 
i = 1; j = 1
 
sqc = set()
 
while i ** 2 <= 10 ** 9:
    sqc.add(i ** 2)
    i += 1
 
while j ** 3 <= 10 ** 9:
    sqc.add(j ** 3)
    j += 1
 
sqc = list(sqc)
sqc.sort()
 
 
for _ in range(int(input())):
    n = int(input())
 
    print(bisect.bisect(sqc, n))
 
 
 