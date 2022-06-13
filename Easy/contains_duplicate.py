# Link: https://leetcode.com/problems/contains-duplicate/
# Runtime: 835 ms
# Memory Usage: 26 MB

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        if len(nums) == len(numsSet):
            return False
        return True