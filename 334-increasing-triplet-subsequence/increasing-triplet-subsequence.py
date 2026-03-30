class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = float('inf')
        l = float('inf')
        for i in range(len(nums)):
            if s >= nums[i]:
                s = nums[i]
            elif s < nums[i]:
                if l >= nums[i]:
                    l = nums[i]
                else: 
                    return True

        return False