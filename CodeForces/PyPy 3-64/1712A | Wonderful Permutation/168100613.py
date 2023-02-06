for case in range(int(input())):
    n, k = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]
 
    '''
    sum_i = 0 to k-1 p[i] contains 1, 2, 3, ..... 
 
    n = 3, k = 1, 2,3,1 -> 1,3,2 0 are in...need 1 so 1 swap
 
    n = 3, k = 3 1,2,3 -> 1,2,3   3 are in...need 3 so 3 - 3 = 0 swap
 
    4 2
 
    3 4 1 2    0 in need 2 so 2 - 0 swap
 
    1 1
 
    1 1 in need 1 so 1 - 1 = 0 swap
 
    see how many of 1 thru k are in the first few 
 
    '''
    found = set()
    for i in range(k):
        if 1 <= p[i] <= k:
            found.add(p[i])
 
    print(k - len(found))