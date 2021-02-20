# 84. Largest Rectangle in Histogram
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack, res = [], 0
        for i in range(len(heights)):
            count = 1
            while stack and stack[-1] > heights[i]:
                res, count = self.compute(stack, res, count)
            for j in range(count):
                stack.append(heights[i])
        count = 1
        while stack:
            res, count = self.compute(stack, res, count)
        return res
    
    def compute(self, stack, res, count):
        temp = stack.pop()
        res = max(res, temp* count)
        count += 1
        return res, count