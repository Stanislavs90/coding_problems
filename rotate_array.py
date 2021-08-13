from typing import List

"""
Input: nums = [1,2,3,4,5,6,7], k = 3

              [5,6,7,1,2,3,4]


Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

index = 0,1,2,3,4,5,6
nums = [1,2,3,4,5,6,7] , k=3
              i     j
       
i = 0
j = 3

swap 
i++
j++

if j greater than max index of array 
mod j by length of array

stop when i == k
----------------------------------------------


for i in range(len(nums)):
    new_index = i + k 
    if new_index > len(nums)-1:
        new_index % len(nums)-1
    nums = nums[new_index]

"""
nums = [1,2,3,4,5,6,7]
      #[7,1,2,3,4,5,6]

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         index_length = len(nums) -1 
#         for i in range(len(nums)):
#             new_index = i + k 
            
#             if new_index > index_length:
#                 new_index = new_index % index_length
#             nums[new_index]




# Index out of range
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        reverse whole array 
        reverse from k index on 
        reverse before k index
        """
        start = 0 
        end = len(nums) -1

        self.helper(start,end, nums)
        self.helper(k, end, nums)
        self.helper(start,k-1, nums)

    def helper(self, start, end, nums):
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1



# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         reverse whole array 
#         reverse from k index on 
#         reverse before k index
#         """
#         start = 0 
#         end = len(nums) -1

#         self.helper(start,end)
#         self.helper(k, end)
#         self.helper(start,k-1)

#     def helper(self, start, end):
#         while start < end:
#             nums[start], nums[end] = nums[end], nums[start]
#             start += 1
#             end -= 1


s = Solution()
s.rotate(nums,2)
print(nums)




