lst = [5, 7, 2, 6, 3, 5, 9, 29, 43, 33, 32, 8]
lst_sorted = [6, 10, 12, 18, 29, 32, 55, 61]
def findRange(lst):
    minItem = lst[0]
    maxItem = lst[0]
    for item in lst:
        if item < minItem:
            minItem = item
        if item > maxItem:
            maxItem = item
    return maxItem - minItem

print(findRange(lst))

def findRangeSorted(lst):
    return lst[len(lst)-1] - lst[0]

print(findRangeSorted(lst_sorted))
