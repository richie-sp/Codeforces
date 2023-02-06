for case in range(int(input())):
    c1,c2 = [x for x in input()]
    c3,c4 = [x for x in input()]
 
    all_colors = set([c1,c2,c3,c4])
 
    print(len(all_colors) - 1)