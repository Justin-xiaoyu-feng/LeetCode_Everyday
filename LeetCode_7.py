# 7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] == '-':
            res = str(x)[1:]
            result = int('-' + res[::-1])
        else:
            result = int(str(x)[::-1])
        if abs(result) > 2**31 - 1:
            return 0
        else:
            return result