class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        store=[]
        r=""
        for i in s:
            if i.lower() in ["a", "e", "i", "o", "u"]:
                #icecream - [i,e,e,a]
                store.append(i)
        store.reverse()
        for i in s:
            if i.lower() in ["a", "e", "i", "o", "u"]:
                r=r+store[0]
                store.pop(0)
            else:
                r=r+i

        return r