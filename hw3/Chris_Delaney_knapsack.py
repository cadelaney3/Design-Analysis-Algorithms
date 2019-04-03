# Chris Delaney
# Algorithms
# Assignment 3, Knapsack problem

import math

# input: 
#   set: a list
# output: a list ofall possible subset of input list
def powerset(set):
    pset_length = int(math.pow(2, len(set)))
    pset = []
    
    for bit in range(0, pset_length):
        subset = []
        for i in range(0, len(set)):
            if ((bit & (1 << i)) > 0):
                subset.append(set[i])
        pset.append(subset)
    return pset

# input: 
#   items: 2D list of items of form [weight, cost]
#   max_weight: maximum weight the knapsack can hold
# output: a tuple containing a list containing total weight
#   and cost of of optimal solution and a list containing the 
#   indicices of the items used for the optimal solution
def knapsack(items, max_weight):
    pset = powerset(items)
    optimal = []
    optimal_indices = []
    for i in range(0, len(pset)):
        weight = 0
        cost = 0
        indices = []
        for j in range(0, len(pset[i])):
            if (pset[i][j] != []):
                weight += pset[i][j][0]
                cost += pset[i][j][1]
            for k in range(0, len(items)):
                if pset[i][j] == items[k]:
                    indices.append(k)
        if (optimal == []):
            if weight <= max_weight:
                optimal = [weight, cost]
                optimal_indices = indices
        else:
            if weight <= max_weight and cost > optimal[1]:
                optimal = [weight, cost]
                optimal_indices = indices
    return (optimal, optimal_indices)

if __name__ == "__main__":
    max_weight = input("Enter max weight that can be held: ")
    num_items = input("Enter number of items to consider: ")
    items = []
    for i in range(0, int(num_items)):
        weight = input("Enter item " + str(i) + " weight: ")
        cost = input("Enter item " + str(i) + " cost: ")
        items.append([int(weight), int(cost)])

    print("items: ", items)
    knapsack_results = knapsack(items, int(max_weight))
    print("")
    print("weight = ", knapsack_results[0][0])
    print("cost = ", knapsack_results[0][1])
    print("indices = ", knapsack_results[1])


            


'''
set = ['a', 'b', 'c']
items = [[10,4], [7,42], [3,12], [4,40], [5,25]]
#powerset(items)
#print(powerset(set))
print(knapsack(items, 5, 10))
'''    
