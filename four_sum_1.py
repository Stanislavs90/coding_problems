from typing import List

array = [7,6,4,-1,1,2]


def fourNumberSum(array, targetSum):
	m = {}
	result = []
	
    # skip first and final values 
    # first value = nothing in hash table
    # second value = nothing after it 

	for i in range(1, len(array)-1):
		for j in range(i + 1, len(array)):
			current_sum = array[i] + array[j]
			diff = targetSum - current_sum
            # to make sure we don't input the value twice
			if diff in m:
				for pair in m[diff]:
					result.append(pair + [array[i], array[j]])
		
		for k in range(0,i):
			current_sum = array[i] + array[k]
			if current_sum not in m:
				m[current_sum] = [[array[k], array[i]]]
			else:
				m[current_sum].append([array[k],array[i]])
	return result

print(fourNumberSum(array, 16))