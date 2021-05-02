# 面试题 01.06. 字符串压缩
class Solution:
    def compressString(self, S: str) -> str:
        res = ''
        i = 0
        while i < len(S):
            temp = S[i]
            count = 1
            while i+1 < len(S) and S[i+1] == temp:
                count += 1
                i += 1
            res += temp
            res += str(count)
            i += 1
        if len(res) < len(S):
            return res
        else:
            return S