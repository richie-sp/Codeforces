from sys import stdin
input = stdin.readline
 
for case in range(int(input())):
    _ = input()
    x = []; y = []; slopes = []
    for l in range(3):
        xi, yi = map(int, input().split())
        x.append(xi); y.append(yi)
 
    for i in range(3):
        for j in range(i + 1, 3):
            x1, y1 = x[i], y[i]
            x2, y2 = x[j], y[j]
 
            try:
                slopes.append((y2 - y1)/(x2 - x1))
            except:
                slopes.append(float('inf'))
 
    if 0 in slopes and float('inf') in slopes:
        print('nO')
    else:
        print('yEs')