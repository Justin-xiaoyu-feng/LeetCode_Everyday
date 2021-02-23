# 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # double pointer
        if len(height) < 2:
            return 0
        i,j = 0, len(height) - 1
        res = 0
        while j > i:
            area = min(height[i], height[j]) * (j-i)
            if area > res:
                res = area
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return res