# Link: https://leetcode.com/problems/palindrome-number/
# Runtime: 69ms
# Memory: 14mb

class Solution:
    def isPalindrome(self, x: int) -> bool:
        sx = str(x)

        if x < 0:
            return False
        elif sx == sx[::-1]:
            return True
        else:
            return False   