class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1[0]=='-':
            num1.remove(num1[0])
        if num2[0]=='-':
            num2.remove(num2[0])
        
        x=int(num1)
        y=int(num2)
        
        result=x+y
        return str(result)
        