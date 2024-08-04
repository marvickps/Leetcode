class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # result=[]
        # for i in range(len(nums)):
        #     result.append(nums[nums[i]])

        # return result

        result = [0] * len(nums)

        for i in nums:
            result[i] = nums[nums[i]]

        return result