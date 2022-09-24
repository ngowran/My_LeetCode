#Link: https://leetcode.com/problems/valid-palindrome/
#Runtime O(n)
#Memory O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s += char
        
        for i in range(0, len(new_s) // 2):
            if new_s[i] != new_s[-(i + 1)]:
                return False
        return True