l1 = [1,2,3]
l2 = [3,2,1]
l3 = [3,1,2]

input_raw_list = [l1, l2, l3]

def list_sorting_checker(input_list):
    desc = False
    asc = False
    changed = False

    for i, el in enumerate(input_list[1:]):
        if changed:
            break
        if el > input_list[i]:
            if desc:
                changed = True
                desc = False
                break
            asc = True
            continue
        elif el < input_list[i]:
            if asc:
                changed = True
                asc = False
                break
            desc = True
            continue
    if asc:
        return 'list has asc order'
    if changed:
        return'list has random order'
    else:
        return'list has desc order'

for i in input_raw_list:
    result = list_sorting_checker(input_raw_list)
    print(result)