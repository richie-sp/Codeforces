from sys import stdin
import bisect 
input = stdin.readline
 
 
 
# Python3 program to count inversions: This function is copied from geeksforgeeks I'm too lazy
  
def mergeSort(arr, n):
    temp_arr = [0]*n
    return _mergeSort(arr, temp_arr, 
                      0, n - 1)
  
def _mergeSort(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right)//2
        inv_count += _mergeSort(arr, temp_arr, 
                                left, mid)
        inv_count += _mergeSort(arr, temp_arr, 
                                mid + 1, right)
        inv_count += merge(arr, temp_arr, 
                           left, mid, right)
    return inv_count
  
def merge(arr, temp_arr, left, mid, right):
    i = left     
    j = mid + 1 
    k = left     
    inv_count = 0
  
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1
  
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
          
    return inv_count
 
#___________________ above code is copied from online _________________________
 
def inv(a, m):
    if(a == 1):
        return 1
    return int((1 - inv(m % a, a) * m) / a + m)
 
n = int(input())
p = list(map(int, input().split()))
 
 
ans = 0; neg_ct = 0; mod = 998244353; non_negs = []; remaining_nums = set([i for i in range(1, n + 1)])
for e in p:
    if e == -1: 
        neg_ct += 1
    else:
        non_negs.append(e); remaining_nums.remove(e)
 
 
 
remaining_nums = list(remaining_nums)
ans += (neg_ct * (neg_ct - 1) * inv(4, mod)); ans %= mod
 
non_neg_inversions = mergeSort(non_negs, len(non_negs))
ans += non_neg_inversions; ans %= mod
 
if neg_ct > 0:
    total_negs = neg_ct; neg_ct = 0
    for ind, elem in enumerate(p):
        if elem == -1:
            neg_ct += 1; continue
 
        negs_before = neg_ct; negs_after = total_negs - neg_ct
        #at this point you want the values filled with negs before to be greater than elem and the values filled with negs after to be less than elem
        ind = bisect.bisect(remaining_nums, elem)
        #prob before is ind/len(remaining_nums) ... prob after is 1 - prob before
        p_after = ind * inv(len(remaining_nums), mod); p_before = 1 - p_after; p_before %= mod; p_after %= mod
        ans += (p_before * negs_before + p_after * negs_after); ans %= mod
 
print(ans)
 
 
 