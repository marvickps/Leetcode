class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = 0
        r = 1
        result = []

        intervals.sort()

        while r < len(intervals):
            if intervals[l][1] >= intervals[r][0]:
                intervals[l][1] = max(intervals[l][1], intervals[r][1])
                r += 1

            else:
                result.append(intervals[l])
                l = r
                r += 1

        result.append(intervals[l])

        return result
