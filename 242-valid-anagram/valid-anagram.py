class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = sorted(s)
        temp2 = sorted(t)
        if temp == temp2:
            return True
        else:
            return False
        
