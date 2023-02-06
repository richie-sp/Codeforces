from sys import stdin
import string
input = stdin.readline 
 
n = int(input())
 
ch_by_val = {i + 1: ch for i, ch in enumerate(string.ascii_uppercase)}; ch_by_val[0] = 'Z'
val_by_ch = {ch: i + 1 for i, ch in enumerate(string.ascii_uppercase)}; val_by_ch['Z'] = 0
 
# print(val_by_ch)
# print(ch_by_val)
 
for line in range(n):
    word = input()[:-1]
    r_pos = None; c_pos = None
    for ind, ch in enumerate(word):
        if ch == 'R' and r_pos is None:
            r_pos = ind
        if ch == 'C' and r_pos is not None and c_pos is None:
            c_pos = ind
 
    if r_pos is not None and c_pos is not None and c_pos > r_pos + 1 and word[r_pos + 1] in '0123456789':
        row_num = int(word[r_pos + 1: c_pos]); col_num = int(word[c_pos + 1:])
        prefix = []
        while col_num > 0:
            rem = col_num % 26
            prefix.append(ch_by_val[rem])
            if rem == 0:
                col_num -= 26
            else:
                col_num -= rem
            col_num //= 26
 
        prefix = prefix[::-1]
        prefix = ''.join(prefix)
        print(prefix + str(row_num))
    else:
        first_num_ind = None
        for ind, ch in enumerate(word):
            if ch in '01233456789':
                first_num_ind = ind; break
 
        row_num = word[first_num_ind:]
        col_num = 0; exp = 0
        for i in range(first_num_ind - 1, -1, -1):
            coef = val_by_ch[word[i]]
            if coef == 0: coef = 26
            col_num += coef * 26 ** exp; exp += 1
 
        print('R' + str(row_num) + 'C' + str(col_num))