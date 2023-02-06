from sys import stdin
input = stdin.readline
 
for c in range(int(input())):
    a = list(map(int, input()[:-1]))
 
    evens = []; odds = []
 
    for elem in a:
        if elem % 2 == 0:
            evens.append(elem)
        else:
            odds.append(elem)
 
    answer = []; e = 0; o = 0
 
    while e < len(evens) or o < len(odds):
        if e == len(evens):
            answer.append(str(odds[o]))
            o += 1
        elif o == len(odds):
            answer.append(str(evens[e]))
            e += 1
        elif odds[o] < evens[e]:
            answer.append(str(odds[o]))
            o += 1
        elif evens[e] < odds[o]:
            answer.append(str(evens[e]))
            e += 1
 
 
    print(''.join(answer))