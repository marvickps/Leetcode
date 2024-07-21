class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        listSum={0:1}
        count=0
        currentSum=0

        for i in range(len(nums)):
            currentSum += nums[i]

            if currentSum - k in listSum:
                count += listSum[currentSum - k]

            if currentSum in listSum:
                listSum[currentSum] += 1
            else:
                listSum[currentSum] = 1

        return count
        