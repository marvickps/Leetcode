class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = ""
        count = 1

        for i in range(1, len(chars)): 
            if chars[i] == chars[i - 1]: #a1 == a0,a2==a1,b3!=a2
                count += 1 #2
            else: 
                s += chars[i - 1]  # s=a
                if count > 1:
                    s += str(count)
                count = 1

        s += chars[-1]
        if count > 1:
            s += str(count)

        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)