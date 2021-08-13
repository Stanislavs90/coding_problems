from typing import List


nums = [0,0,1,1,1,2,2,3,3,4]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Input: nums = [0,0,1,1,1,2,2,3,3,4]
                       i     j           
                       
                      [0,1,2,3,0,2,1,3,1,4]
                               i         j 
        i = 0 
        j = 1
        while j < len(nums)

        if i == j:
            i++
            j++
        if i != j: 
            if j + 1 == j 
            j++
            
            else:
                swap
                i++
                j++
        if j == len(nums)-1:
            swap
        
        return i , nums[i:]
        
        Output: 5, nums = [0,1,2,3,4]
        """
        i = 0
        for j in range(1,len(nums)):
            
            if nums[i] == nums[j]:
                j+=1
                i+=1
            # index out of range
            if nums[j+1] == nums[j]: 
                j+=1
            else:    
                nums[i], nums[j] = nums[j], nums[i]
                i+= 1
                j+= 1
            if j == len(nums) -1:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    break
              
        return i, nums[:i]
    
    def removeDuplicates1(self, nums: List[int]) -> int:

        if nums is None or len(nums) < 1:
            return None

        uniq = 1
        is_prev_dup = False

        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                if uniq != i:
                    nums[uniq] = nums[i]
                uniq=uniq+1

        return uniq
            

s = Solution()

uniq = s.removeDuplicates1(nums)
print(uniq)
for i in range(0, uniq):
    print(nums[i])