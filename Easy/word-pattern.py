# Link: https://leetcode.com/problems/word-pattern/
# Runtime: 37 ms
# Memory: 13.9 mb

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = {}
        answer = []

        s_list = s.split()

        if len(pattern) != len(s_list):
            return False

        for i, value in enumerate(pattern):
            if value not in pattern_dict.keys() and s_list[i] not in pattern_dict.values():
                pattern_dict[value] = s_list[i]
            elif value in pattern_dict.keys() and s_list[i] != pattern_dict[value]:
                return False
            elif value not in pattern_dict.keys() and s_list[i] in pattern_dict.values():
                pattern_dict[value] = "null"

        print(pattern_dict)
        for c in pattern:
            answer.append(pattern_dict[c])

        if " ".join(answer) == s:
            return True


