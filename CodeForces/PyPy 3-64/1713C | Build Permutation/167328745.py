import math
from collections import defaultdict
import math
for case in range(int(input())):
    n = int(input())
    squares = [i ** 2 for i in range(0, int(math.ceil(math.sqrt(2 * n))))]
    mapping = [[] for i in range(n)]
    for i in range(n-1, -1, -1):
        for square in squares:
            if 0 <= square - i <= n-1:
                mapping[i].append(square - i)
 
            
    found = set()
    rev_ans = []
    for elem in reversed(mapping):
        ptr = len(elem) - 1
        while elem[ptr] in found:
            ptr -= 1
        #postcondition ptr in found
        rev_ans.append(str(elem[ptr]))
        found.add(elem[ptr])
 
    # print(mapping)
    print(' '.join(rev_ans[::-1]))