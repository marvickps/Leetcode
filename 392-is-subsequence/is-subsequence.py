class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count =0

        for i in t:
            if count < len(s) and s[count] == i:
                count += 1

        return count == len(s)