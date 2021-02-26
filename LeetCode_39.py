class Solution:
     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        import copy
        result = []
        def dfs(i, candidates, target, tmp=[]):
                for j in range(i, len(candidates)):
                    if sum(tmp) < target:
                        tmp.append(candidates[j])
                        dfs(j, candidates, target, tmp)
                        if sum(tmp) == target:
                            result.append(copy.deepcopy(tmp))
                        tmp.pop() 

        candidates = sorted(candidates)
        dfs(0, candidates, target)
        return result