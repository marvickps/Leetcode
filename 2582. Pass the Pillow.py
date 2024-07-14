class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        cycleLength=2*(n-1)
        cycleCount = time % cycleLength
        if cycleCount <n:
            return cycleCount+1
        else:
            return (2 * n) - (cycleCount + 1)
            
        
