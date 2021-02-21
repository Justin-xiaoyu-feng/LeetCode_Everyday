# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dp approach, dp[i]: max length of substring without repeating end with s[i]
        if len(s) < 2:
            return len(s)
        dp = [0 for i in range(len(s))]
        dp[0] = 1
        for i in range(1,len(s)):
            if s[i] not in s[i-dp[i-1]:i]:
                dp[i] = dp[i-1] + 1
            else:
                index = s[i-dp[i-1]: i].index(s[i])
                l = len(s[i-dp[i-1]: i][index+1:]) + 1
                dp[i] = max(l, 1)
        return max(dp)