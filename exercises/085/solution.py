

def sort_a_list(l):
    new_list = l[:]
    ok = False
    while(not ok):
        ok = True
        for i in reversed(range(1,len(l))):
            if(new_list[i-1] < new_list[i]):
                temp = new_list[i-1]
                new_list[i-1] = new_list[i]
                new_list[i] = temp
                ok = False
    return new_list


def sort_by_mark(l):
    return sort_a_list(l)


def sort_by_name(l):
    new_list = permute(l)
    new_list2 = sort_a_list(new_list)
    return permute(new_list2)


def permute(l):
    new_list = l[:]
    for i in range(len(l)):
        temp = new_list[i]
        new_list[i][0] = temp[1]
        new_list[i][1] = temp[0]
    return new_list