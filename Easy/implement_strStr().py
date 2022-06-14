# Link: https://leetcode.com/problems/implement-strstr
# Runtime: 50 ms
# Memory Usage: 13.8 MB

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i, value in enumerate(haystack):
            if value == needle[0] and haystack[i : i + len(needle)] == needle:
                return i
        return -1
        