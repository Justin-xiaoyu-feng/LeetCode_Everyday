# 1720. 解码异或后的数组
# 一个数xor两次就消除影响，变回原来本身的数了

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for ele in encoded:
            res.append(ele ^ res[-1])
        return res