list1 = [2, 5, 5, 5]
list2 = [2, 2, 3, 5, 5, 7]

def commonelems(l1, l2):
    shortlist = []
    longlist = []
    commonlst = []
    if len(l1) < len(l2):
        shortlist = l1
        longlist = l2
    else:
        shortlist = l2
        longlist = l1
    for item1 in shortlist:
        for item2 in longlist:
            if item1 == item2:
                commonlst.append(item1)
                longlist.remove(item2)
                break
    return commonlst

print(commonelems(list1, list2))
