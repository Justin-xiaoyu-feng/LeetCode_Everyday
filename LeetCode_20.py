# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')','[':']','{':'}'}
        stack = []
        for char in s:
            if char in d:
                stack.append(d[char])
            else:
                if not stack or stack[-1] != char:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        return False