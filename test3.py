from typing import List

array = [i for i in range(1,21)]
print(array)


#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# x  p  p  x  p  x  p  x  x   x  p    x       x   x  x        x       x 

"""
results = []

start at element 2
    if element not false append to result
    
    loop over rest of array 
        if select element // i-th array element == 0:
            mark as false

"""


def prime_numbers(array):
    result = []
    multiples = []
    for i in range(2,len(array)+ 1):
        if i not in multiples:
            result.append(i)
            for j in range(i*i, len(array)+1, i):
                multiples.append(j)
       
    return result


print(prime_numbers(array))