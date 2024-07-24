class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        i=1
        
        while i < len(intervals):
            intervals.sort()
            if intervals[i-1][1]>=intervals[i][1] or intervals[i-1][1] >= intervals[i][0]:
                intervals.insert(0,[min(intervals[i-1][0],intervals[i][0]),max(intervals[i-1][1],intervals[i][1])])
                intervals.remove(intervals[i])
                intervals.remove(intervals[i])
            
            else:i += 1
            


        return intervals
        
        