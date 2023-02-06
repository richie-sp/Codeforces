 
def backtrack(partial_candidate: str, final_str: str, seen: set) -> bool:
    # print(f"Partial Candidate {partial_candidate}")
    if partial_candidate in seen:
        return
    else:
        seen.add(partial_candidate)
    if len(partial_candidate) == len(final_str):
        return True
    i = len(partial_candidate)
    #start building from i
    
    can_add = False
    anss = []
    for addn in ['aa', 'aaa', 'bb', 'bbb']:
        if len(partial_candidate) + len(addn) <= len(final_str):
            if len(addn) == 3:
                if addn[0] == final_str[i] and addn[1] == final_str[i+1] and addn[2] == final_str[i+2]:
                    anss.append(backtrack(partial_candidate + addn, final_str, seen))
                    can_add = True
            else:
                if addn[0] == final_str[i] and addn[1] == final_str[i+1]:
                    anss.append(backtrack(partial_candidate + addn, final_str, seen))
                    can_add = True
 
    if not can_add:
        return False
 
    return True in anss
 
 
 
 
 
for case in range(int(input())):
    s = input()
    print('Yes') if backtrack('', s, set()) else print('No')