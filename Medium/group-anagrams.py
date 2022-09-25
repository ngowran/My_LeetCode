#Link: https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dic = {}
        final_list = []
        
        for word in strs:
            sort_word = "".join(sorted(word))
            if sort_word in anagram_dic:
                anagram_dic[sort_word].append(word)
            else:
                anagram_dic[sort_word] = [word]
        
        for value in anagram_dic.values():
            final_list.append(value)
                
        return final_list     
