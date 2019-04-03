# Chris Delaney
# hw4: dynamic knapsack and memoization

# Execution time for algorithm d (4 items): 0.000121 s
# Execution time for algorithm f (4 items): 0.000066 s
# Time for d (8 items): 0.00014 s
# Time for f (8 items): 0.000106 s
# Time for d (16 items): 0.000817 s
# Time for f (16 items): 0.000621 s

# Conclusion: f executes faster

import math
import time


def d(items, max_weight):
    F = []
    for m in range(len(items)+1):
        F.append([0]*(max_weight+1))
    for i in range(0, len(items)+1):
        for j in range(0, max_weight+1):
            if i == 0 or j == 0:
                F[i][j] = 0
            elif j - items[i-1][0] >= 0:
                F[i][j] = max(F[i-1][j], items[i-1][1]+F[i-1][j-items[i-1][0]])
            else:
                F[i][j] = F[i-1][j]
    return F

def f(i, j, items, F):
    if F[i][j] < 0:
        value = 0
        if j < items[i-1][0]:
            value = f(i-1, j, items, F)
        else:
            value = max(f(i-1, j, items, F), items[i-1][1]+f(i-1, j-items[i-1][0], items, F))
        F[i][j] = value
    return F[i][j]

if __name__ == "__main__":

    algorithm = input()
    max_weight = int(input())
    num_items = int(input())
    items = []
    for item in range(int(num_items)):
        weight = input()
        cost = input()
        items.append((int(weight), int(cost)))
    print()

    F = []
    if algorithm == 'd':
        start = time.time()
        F = d(items, max_weight)
        end = time.time()
        print("\nExecution time: %f\n" % (end-start))

    else:
        for m in range(len(items)+1):
            if m == 0:
                F.append([0]*(max_weight+1))
            else:
                F.append([-1]*(max_weight+1))
                F[m][0] = 0
        start = time.time()
        f(len(F)-1, max_weight, items, F)
        end = time.time()
        print("\nExecution time: %f\n" % (end-start))
       
    total_count = 0
    comp_count = 0
    for i in range(num_items+1):
        for j in range(max_weight+1):
            if F[i][j] != -1:
                comp_count += 1
            total_count += 1
            print(F[i][j], end="\t")
        print()
    
    if algorithm == 'f':
        print("\nPercentage of table computed (including zeros): %.2f%%\n" % (comp_count/total_count * 100))