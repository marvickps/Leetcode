class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_t_To_s = {}
        map_s_To_t = {}
        for i in range(len(s)):
            if t[i] in map_t_To_s:
                if s[i]!=map_t_To_s[t[i]]:
                    return False
            else:
                map_t_To_s[t[i]]=s[i]

            if s[i] in map_s_To_t:
                if t[i]!=map_s_To_t[s[i]]:
                    return False
            else:
                map_s_To_t[s[i]]=t[i]

        return True