class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_score = 0
        
        for i in range(1, len(s)):
            countleft = 0
            countRight = 0
            for j in s[:i]:
                if j == '0':
                    countleft += 1
            for j in s[i:]:
                if j == '1':
                    countRight += 1
            left = countleft
            right = countRight
            max_score = max(max_score, left + right)
        return max_score
