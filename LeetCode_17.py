# 17. Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': 'abc'
            ,'3': 'def'
            ,'4': 'ghi'
            ,'5': 'jkl'
            ,'6': 'mno'
            ,'7': 'pqrs'
            ,'8': 'tuv'
            ,'9': 'wxyz'}
        res = []
        for c in digits:
            if not res:
                res = list(d[c])
            else:
                temp = []
                for ele in res:
                    for char in list(d[c]):
                        temp.append(ele + char)
                res = list(set(temp))
        return res