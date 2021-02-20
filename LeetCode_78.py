# 78. Subsets
import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return [[]]
        for i in range(len(nums) + 1):
            for ele in itertools.combinations(nums, i):
                if list(ele) not in res:
                    res.append(list(ele))
        return res

# cascading
# 1. start from empty subset: []
# 2. add first ele in res: [],[1]
# 3. update current res with second ele, add to res: [], [1] + [2], [1,2]
# ...
'''
def subsets(nums):
    res = [[]]
    if not nums:
        return res
    for ele in nums:
        ######## output += [curr + [num] for curr in output]
        temp = res
        for i in range(len(temp)):
            temp[i].append(ele)
        res.append(temp)
    return res
'''