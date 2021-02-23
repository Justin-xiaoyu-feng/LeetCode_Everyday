# 15. 3Sum
class Solution:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        num = sorted(num)
        res = []
        for i in range(len(num) - 2):
            j,k = i+1, len(num)-1
            while k > j:
                s = num[i] + num[j] + num[k]
                temp = [num[i], num[j], num[k]]
                if s == 0 and temp not in res:
                    res.append(temp)
                elif s > 0:
                    k -= 1
                else:
                    j += 1
        return res
