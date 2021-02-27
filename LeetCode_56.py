class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort array based on start time, curr = starting one, if the start time of next one
        # in interval, update curr. If not, res += curr, replace curr.
        intervals.sort(key=lambda x:x[0])
        curr = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] in range(curr[0], curr[1]+1):
                curr = [min(intervals[i][0], curr[0]), max(intervals[i][1], curr[1])]
            else:
                res.append(curr)
                curr = intervals[i]
        res.append(curr)
        return res