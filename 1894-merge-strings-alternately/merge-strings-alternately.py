class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        r = ""
        l=0


        if len(word1)>len(word2):
            l = len(word1)
        else: 
            l = len(word2)
            
        for i in range(0,l):
            if i < len(word1):
                r=r+word1[i]
            if i < len(word2):
                r=r+word2[i]
            
        return r
        