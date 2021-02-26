class Solution:
    def trap(self, height: List[int]) -> int:
        i,j = 1, len(height) - 2
        if j < i:
            return 0
        l, r = height[0], height[-1]
        res = 0
        while i <= j:
            if l > r:
                r = max(r, height[j])
                res += r - height[j]
                j -= 1
            else:
                l = max(l, height[i])
                res += l - height[i]
                i += 1
        return res
