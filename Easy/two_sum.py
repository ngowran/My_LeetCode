# Link: https://leetcode.com/problems/two-sum
# Runtime: 95 ms, faster than 56.49% of Python3 online submissions for Two Sum.
# Memory Usage: 15.1 MB, less than 49.32% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_of_nums = {}
        i = 0
        while i < len(nums):
            second_n = target - nums[i]
            if second_n in dict_of_nums:
                return [dict_of_nums[second_n], i]
            else:
                dict_of_nums[nums[i]] = i
            i += 1
        
