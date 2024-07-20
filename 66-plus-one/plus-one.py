class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #6999
        n = len(digits)

        if 0 <= digits[n - 1] <= 8:
            digits[n - 1] = digits[n - 1] + 1
        else:
            for i in range(n - 1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                    if i == 0:
                        digits.insert(0, 1)
                else:
                    digits[i] = digits[i] + 1
                    break

        return digits

                
        