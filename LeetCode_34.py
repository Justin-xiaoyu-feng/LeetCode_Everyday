class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # double pointer
        i, j = 0, len(nums)-1
        while i < len(nums) and nums[i] != target:
            i += 1
        while j >= 0 and nums[j] != target:
            j -= 1
        if j < i:
            return [-1, -1]
        elif j == i and nums[j] == target:
            return [i, j]
        else:
            return [i, j]
        # 2分查找
        