from typing import List

# value, weight
items = [[1,2],[4,3],[5,6][6,7]]
# max capacity
capacity = 10

"""
dp = [0] * len(items)


"""

def knapsackProblem(items, capacity):
                        #[[columns] rows]
    knapsackValues = [[0 for x in range(0, capacity +1)] for y in range(0, len(items) + 1)]
    # build the array
    for i in range(1, len(items) + 1):
        # i - 1 because we have an empty row on top
        currentWeight = items[i - 1][1]
        currentValue = items[i - 1][0]

        for c in range(0, capacity + 1):
            
            if currentWeight > c:
                knapsackValues[i][c] = knapsackValues[i - 1][c]
            else:
                knapsackValues[i][c] = max(knapsackValues[i - 1][c], knapsackValues[i - 1][c - currentWeight] + currentValue)

    return [knapsackValues[-1][-1], getKnapSackItems(knapsackValues, items)]

def getKnapSackItems(knapsackValues, items):
    sequence = []
    i = len(knapsackValues) - 1
    c = len(knapsackValues[0]) - 1
    while i > 0:
        if knapsackValues[i][c] == knapsackValues[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= item[i - 1][1]
            i -= 1 
        if c==0:
            break
    return list(reversed(sequence))