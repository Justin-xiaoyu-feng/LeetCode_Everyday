# 5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        l = 0
        res = ''
        for i in range(len(s) - 1):
            temp1 = 1
            temp2 = 0
            k = 1
            while i-k >= 0 and i+k < len(s) and s[i-k] == s[i+k]:
                k += 1
                temp1 += 2
            if s[i] == s[i+1]:
                temp2 = 2
                j = 1
                while i-j >= 0 and i+1+j < len(s) and s[i-j] == s[i+1+j]:
                    j += 1
                    temp2 += 2
            if max(temp1, temp2) > l:
                l = max(temp1, temp2)
                if temp1 > temp2:
                    res = s[i-k+1: i+k]
                else:
                    res = s[i-j+1: i+1+j]
            print(temp1, temp2, i)
        return res