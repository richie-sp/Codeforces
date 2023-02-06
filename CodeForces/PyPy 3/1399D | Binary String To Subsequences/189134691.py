from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    s = [int(ch) for ch in input()[:-1]]
 
    zero_sequences = []; one_sequences = []
 
    counter = 1; ct_by_ind = [-1 for ch in s]
    for ind, dig in enumerate(s):
        if not zero_sequences and not one_sequences:
            if dig == 1:
                one_sequences.append(counter); ct_by_ind[ind] = counter
            else:
                zero_sequences.append(counter); ct_by_ind[ind] = counter
            counter += 1; continue
 
        if dig == 1:
            if zero_sequences:
                old_ct = zero_sequences.pop()
                ct_by_ind[ind] = old_ct
                one_sequences.append(old_ct)
            else:
                one_sequences.append(counter)
                ct_by_ind[ind] = counter
                counter += 1
 
        if dig == 0:
            if one_sequences:
                old_ct = one_sequences.pop()
                ct_by_ind[ind] = old_ct
                zero_sequences.append(old_ct)
            else:
                zero_sequences.append(counter)
                ct_by_ind[ind] = counter
                counter += 1
 
    print(counter - 1)
    print(' '.join(str(ch) for ch in ct_by_ind))
 
 
 
        