class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    # or itertools.permutations
        if len(nums) == 1:
            return [nums]
        n = len(nums)
        res = []
        x = nums[0]
        temp = self.permute(nums[1:])
        for i in range(n):
            for ele in temp:
                res.append(ele[:i] + [x] + ele[i:])
        return res