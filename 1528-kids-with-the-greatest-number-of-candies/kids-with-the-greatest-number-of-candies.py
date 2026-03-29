class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        highest = 0

        returnList = []
        for i in candies:
            if i > highest:
                highest = i


        for i in candies:
            x = i + extraCandies
            if x >= highest:
                returnList.append(True)
            else: 
                returnList.append(False)


        return returnList

    