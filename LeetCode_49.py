class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary approach
        d = {}
        for ele in strs:
            if str(sorted(list(ele))) not in d:
                d[str(sorted(list(ele)))] = [ele]
            else:
                d[str(sorted(list(ele)))].append(ele)
        return d.values()