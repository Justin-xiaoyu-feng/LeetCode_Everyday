# 面试题 01.04. 回文排列
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if not s:
            return True
        count_odd = 0
        for char in set(list(s)):
            if s.count(char) %2 == 1:
                count_odd += 1
        return count_odd <= 1