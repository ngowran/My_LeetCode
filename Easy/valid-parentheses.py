#Link: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {"(": ")",
                   "{": "}",
                   "[": "]"
                  }
        stack = []
        if len(s) < 2:
            return False
        
        for char in s:
            if char in bracket.keys():
                stack.append(char)
            elif char in bracket.values():
                if len(stack) < 1:
                    return False
                elif bracket[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True