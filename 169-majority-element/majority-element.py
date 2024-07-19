class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        h={}
        for i in range(n):
            if nums[i] in h:
                h[nums[i]]+=1
            else:
                h[nums[i]]=1
        for key, value in h.items():
            if value > n/2:
                return key