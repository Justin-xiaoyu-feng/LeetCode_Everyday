# 740. 删除并获得点数
# DP solution, there are cleaner solutions with the same concept.
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(set(nums)) == 1:
            return nums[0] * len(nums)
        if len(set(nums)) == 2:
            [n_1, n_2] = list(set(sorted(nums)))
            if n_2 != n_1 + 1:
                return n_1* nums.count(n_1) + n_2* nums.count(n_2)
            else:
                return max(n_1* nums.count(n_1), n_2* nums.count(n_2))
        s = list(set(sorted(nums)))
        dp = [0 for i in range(len(s))]
        dp[0] = s[0] * nums.count(s[0])
        if s[1] != s[0] + 1:
            dp[1] = dp[0] + s[1] * nums.count(s[1])
        else:
            dp[1] = s[1] * nums.count(s[1])
        for i in range(2, len(s)):
            if s[i] - 1 not in s:
                dp[i] = max(dp[:i]) + s[i] * nums.count(s[i])
            else:
                dp[i] = max(dp[:i-1]) + s[i] * nums.count(s[i])
        return max(dp)