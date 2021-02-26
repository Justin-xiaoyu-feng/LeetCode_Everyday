# 45. Jump Game II
class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        # dp, tle
        if len(nums) <= 1:
            return 0
        dp = [0 for i in range(len(nums))]
        dp[0] = 0
        for i in range(1, len(nums)):
            temp = []
            for j in range(i):
                if j + nums[j] >= i:
                    temp.append(dp[j])
            dp[i] = min(temp) + 1
        return dp[-1]
        '''
        # greedy
        fastest,jump,end = 0,0,0
        for i in range(len(nums) - 1):
            fastest = max(fastest, nums[i] + i)
            if i == end and i != len(nums) - 1:
                jump += 1
                end = fastest
        return jump