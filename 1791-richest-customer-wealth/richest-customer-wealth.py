class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        highest=0
        total =0
        for i in accounts:
            total = sum(i) 
            if highest < total:
                highest = total

        return highest
        