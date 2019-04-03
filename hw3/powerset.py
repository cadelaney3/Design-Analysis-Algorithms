a = ["a", "b", "c", "d"]

def powerSet(A):
    powerset = [[]]
    for i in range(len(A)-1):
        for j in range(len(powerset)):
            powerset.append(powerset[j] + [A[i]])
    for i in range(len(powerset)):
        powerset.append(powerset[i] + [A[len(A)-1]])
    return powerset

print(powerSet(a))