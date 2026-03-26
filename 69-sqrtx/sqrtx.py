class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        l=0
        r=x
        while l <= r:
            mid = (l+r) // 2 #4, 6
            power = mid**2 #16
            if power == x:
                return mid
            elif power < x:
                l = mid + 1 #5
            else:
                r = mid - 1

        return r



            