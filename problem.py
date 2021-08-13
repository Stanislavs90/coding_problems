from typing import List

"""
ch_pointer
counter_pointer

counter = 0
result = []

loop
    if n[i] == n[j]:
        j++
        counter++
        result.append(n[i])
        result.append(counter)

    if n[i] != n[j]:
        i = j


"""
n = 338

class Solution:
    def countAndSay(self, n: int) -> str:
        counter = 0
        result = ''
        my_string = str(n)

        ch_pointer = 0
        counter_pointer =0
        while counter_pointer < len(my_string):
            if my_string[ch_pointer] == my_string[counter_pointer]:
                counter += 1
                counter_pointer += 1
                result += str(my_string[ch_pointer])
            else:
                ch_pointer = counter_pointer
        
        return result




s = Solution()
print(s.countAndSay(n))