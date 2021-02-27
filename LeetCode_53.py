# 53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] >= 0:
                dp[i] = nums[i] + dp[i-1]
            else:
                dp[i] = nums[i]
        return max(dp)