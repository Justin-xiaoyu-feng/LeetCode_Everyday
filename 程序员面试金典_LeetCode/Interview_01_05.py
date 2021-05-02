# 面试题 01.05. 一次编辑
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first)-len(second)) > 1:
            return False
        if len(first) > len(second):
            first, second = second, first
        for i in range(len(first)):
            if first[i] == second[i]:
                continue
            return first[i:] == second[i+1:] or first[i+1:] == second[i+1:]
        return True