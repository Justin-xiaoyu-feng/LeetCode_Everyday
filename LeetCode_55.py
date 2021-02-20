# 55. Jump Game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        dp = [0 for i in range(len(nums))]
        dp[0] = 1
        for i in range(1, len(nums)):
            # changed from for j in range(i), back loop much faster
            for j in range(i-1, -1, -1):
                if dp[j] == 1 and j + nums[j] >= i:
                    dp[i] = 1
                    break
        if dp[-1] == 0:
            return False
        else:
            return True