# 41. First Missing Positive
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = list(filter(lambda x: x>0, nums))
        if not l:
            return 1
        min_ele, max_ele = min(l), max(l)
        if min_ele > 1:
            return 1
        for i in range(min_ele + 1, max_ele):
            if i not in l:
                return i
        return max_ele + 1