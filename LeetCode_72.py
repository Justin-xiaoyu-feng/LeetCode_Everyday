# 72. Minimum Edit Distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]
        
        for i in range(l1+1):
            for j in range(l2+1):
                if j == 0:
                    dp[i][j] = i
                elif i == 0:
                    dp[i][j] = j
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]