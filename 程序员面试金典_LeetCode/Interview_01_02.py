# 面试题 01.02. 判定是否互为字符重排
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        if s1[0] not in s2:
            return False
        else:
            idx = s2.index(s1[0])
            return self.CheckPermutation(s1[1:], s2[:idx] + s2[idx+1:])