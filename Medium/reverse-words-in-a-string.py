#Link: https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip(" ")
        s = s.split(" ")
        new_s = []
        stack = []
        for word in s:
            if word:
                stack.append(word)
                
        while stack:
            new_s.append(stack.pop())
        
        return " ".join(new_s)
