# Link https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# Runtime: 32 ms, faster than 93.51% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
# Memory Usage: 13.9 MB, less than 55.64% of Python3 online submissions for Find N Unique Integers Sum up to Zero.

class Solution:
    def sumZero(self, n: int) -> List[int]:
        my_answer = []
        if n == 1:
            return [0]
        for i in range(1, n):
            my_answer.append(i)
    
        neg = sum(my_answer)
        my_answer.append(neg * - 1)
        return(my_answer)