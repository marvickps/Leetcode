class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """

 
        score = 0
        left_0 = {'0': 0} 
        countRight = 0

        for j in s:
            if j == '1':
                countRight += 1

        right_1 = countRight

        for i in range(len(s) - 1):
            # 0-1, 00-2,0010-3 00100-4
            if s[i] == '0':
                left_0['0'] += 1
            else:
                #0100111-4, 100111-4, 00111-3,0111-3,
                right_1 = right_1 - 1
            score = max(score, left_0['0'] + right_1)

        return score