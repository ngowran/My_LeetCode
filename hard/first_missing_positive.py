# Link: https://leetcode.com/problems/first-missing-positive
# Runtime: 805 ms
# Memory Usage: 69.9 MB

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        smallest = 1
        
        nums = set(nums)
        
        if not nums:
            return smallest
        
        for i in range(1, max(nums)):
            if i not in nums:
                return i
            
        return max(smallest, max(nums) + 1)

# The smallest possible number is 1, 
# if another smallest number is not found in the range,
# then it has to be 1 or the max number in the list + 1,
# if the list is empty the smallest is 1.