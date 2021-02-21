# 8. String to Integer (atoi)
class Solution:
    def myAtoi(self, s: str) -> int:
        new_s = s.strip()
        k = 0
        sign = 1
        if len(new_s) == 0:
            return 0
        if new_s[0] == '-':
            sign = -1
            new_s = new_s[1:]
        elif new_s[0] == '+':
            sign = 1
            new_s = new_s[1:]
        while k < len(new_s) and new_s[k].isdigit():
            k += 1
        if k == 0:
            return 0
        else:
            if int(new_s[:k]) < 2**31:
                return sign*int(new_s[:k])
            elif sign == 1:
                return sign*(2**31 - 1)
            else:
                return sign*(2**31)