# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Runtime: 241 ms
# Memory Usage: 15.4 MB

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1

        i = 0
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                del nums[i]

                if len(nums) == 1:
                    break
                
            else:
                i += 1
        
        print(nums)
        