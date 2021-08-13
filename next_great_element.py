from typing import List
"""
result array
loop over first array
    loop over second array
        find second element

            loop over second array
                see if there is anything greater 
                    if yes
                        append element
                    else 
                        append -1

        if second element not found
            append -1
"""
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            for j in range(len(nums2)):
                if num == nums2[j]:
                    for n in range(j+1, len(nums2)):
                        if nums2[n] > nums2[j]:
                            result.append(nums2[n])
                            break
                        else:
                            result.append(-1)            

        return result


s = Solution()
print(s.nextGreaterElement(nums1, nums2))

