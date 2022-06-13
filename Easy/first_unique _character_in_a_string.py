# Link https://leetcode.com/problems/first-unique-character-in-a-string/
# Runtime: 7394 ms
# Memory Usage: 14.1 MB

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, c in enumerate(s):
            if s.count(c) == 1:
                return i
        return "-1"
        