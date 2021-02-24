# 32. Longest Valid Parentheses
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # dp approach, dp[i] is longest valid parentheses end with s[i]
        # if s[i] is '(', dp[i] is 0, if s[i] is ')' and s[i-1] is '(', dp[i] = dp[i-2] + 2
        # is s[i] is ')' and s[i-1] == ')' and s[i-dp[i-1] -1] == '('
        # dp[i] = dp[i-1] + dp[i-dp[i-1] - 2] + 2
        # eg: ( ) ( ( ( ) ) )
        #     0 2 0 0 0 2 4 8, 8 = dp[6] + dp[1] + 2
        if len(s) < 2:
            return 0
        dp = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                elif i-dp[i-1] - 1 >= 0 and s[i-dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
        return max(dp)