# 面试题 01.01. 判定字符是否唯一
class Solution:
    def isUnique(self, astr: str) -> bool:
        '''
        # use dictionary
        d = {}
        if not astr:
            return True
        for char in astr:
            if char in d:
                return False
            else:
                d[char] = 1
        return True
        '''
        if not astr:
            return True
        for char in astr:
            if astr.count(char) != 1:
                return False
        return True