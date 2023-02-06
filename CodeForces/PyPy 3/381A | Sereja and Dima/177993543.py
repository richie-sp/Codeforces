n = int(input())
 
cards = [int(x) for x in input().split()]
 
ptr1, ptr2 = 0, n - 1
 
s, d = 0, 0
 
turn = 0
while ptr1 <= ptr2:
    if cards[ptr2] > cards[ptr1]:
        if turn % 2 == 0:
            s += cards[ptr2]
        else:
            d += cards[ptr2]
 
        ptr2 -= 1
    else:
        if turn % 2 == 1:
            d += cards[ptr1]
        else:
            s += cards[ptr1]
 
        ptr1 += 1
 
    turn += 1
 
print(f"{s} {d}")
 