class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        lawraList = [1, 1]

        for i in range(2, n+1):
            next_number = lawraList[i - 1] + lawraList[i - 2]
            lawraList.append(next_number)

        return lawraList[n]
        