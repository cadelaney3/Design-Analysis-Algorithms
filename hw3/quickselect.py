a = [4, 1, 10, 8, 7, 12, 9, 2, 15]
a2 = [10, 4, 5, 8, 6, 11, 26]
a3 = [20, 3, 18, 19, 5, 32, 11, 6, 1, 0, 23, 55, 13]

def LomutoPartition(A, l, r):
    p = A[l]
    s = l
    for i in range(l+1, r):
        if A[i] < p:
            s += 1
            A[s], A[i] = A[i], A[s]
    A[l], A[s] = A[s], A[l]
    return s

def quickselect(A, l, r, k):
    s = LomutoPartition(A, l, r)
    while (s != k-1):
        if s == k-1:
            return A[s]
        elif s > (l+k-1):
            s = LomutoPartition(A, l, s)
        else:
            s = LomutoPartition(A, s+1, r)
    return A[s]

print(quickselect(a, 0, len(a), 5))
print(quickselect(a2, 0, len(a2), 3))
print(quickselect(a3, 0, len(a3), 6))