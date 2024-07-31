class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        frequency = {}
        for card in deck:
            if card in frequency:
                frequency[card] += 1
            else:
                frequency[card] = 1

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        frequencies = list(frequency.values())
        group_size = frequencies[0]
        for freq in frequencies[1:]:
            group_size = gcd(group_size, freq)

        return group_size > 1

        
        