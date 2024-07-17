class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strTemp=""
        final=[]
        for i in range(len(digits)):
            strTemp+=str(digits[i])

        num=int(strTemp)
        num+=1
        strTemp=str(num)
        for i in range(0,len(str(num))):
            final.append(int(strTemp[i]))
        
        return final

        