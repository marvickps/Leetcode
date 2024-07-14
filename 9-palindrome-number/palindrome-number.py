class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return 0
        else:
            if x - int(str(x)[::-1]) == 0:
                return 1
            return 0
        

        
        