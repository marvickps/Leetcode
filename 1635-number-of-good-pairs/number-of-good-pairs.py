class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        h2={}
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]] = 0
                h2[nums[i]] = 1
            else:
                h2[nums[i]] += 1
                h[nums[i]] += h2[nums[i]]-1

        sum = 0
        for key, values in h.items():
            sum += values
        return sum
                
            