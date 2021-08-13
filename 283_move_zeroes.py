

from typing import List


nums =[0,1,0,3,12]


# times out
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 1
        
        total = 0
        for num in nums:
            total += num
        if total < 1:
            return nums
                
        while j <= len(nums)-1:
            if nums[i] == 0 and nums[j] == 0:
                j+=1
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i+= 1
                j+= 1


s = Solution()
s.moveZeroes(nums)
print(nums)