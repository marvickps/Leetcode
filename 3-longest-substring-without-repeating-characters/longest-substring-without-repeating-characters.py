class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r = 0
        le = len(s)
        mapp = {}#a:1,b:1,c:1
        temp = 0
        while r<le:
            if s[r] in mapp:
                x = sum(mapp.values())
                mapp = {}
                r=l
                l+=1
                if x > temp:
                    temp = x
                
            else:
                mapp[s[r]] = 1
            r+=1
        if sum(mapp.values()) > temp:
            return sum(mapp.values())
        return temp