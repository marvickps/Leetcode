class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # returnlist = s.split(" ")
        # returnlist.reverse()
        # x = len(returnlist)-1
        # i=0
        # while i <= x:
        #     if returnlist[i] == "":
        #         returnlist.pop(i)
        #         x-=1
        #     else:
        #         i+=1
            
        # return " ".join(returnlist)
        returnlist = []
        word = ""

        for i in s:
            if i == " ":
                if word != "":
                    returnlist.append(word)
                    word = ""  
            else:
                word=word+i
        if word != "":
            returnlist.append(word)
        
        returnlist.reverse()
        return " ".join(returnlist)