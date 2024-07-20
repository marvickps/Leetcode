class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        total_length = len(nums)
        
        if total_length % 2 == 0:
            median = (nums[total_length // 2 - 1] + nums[total_length // 2]) / 2.0
        else:
            median = nums[total_length // 2]
        
        return median