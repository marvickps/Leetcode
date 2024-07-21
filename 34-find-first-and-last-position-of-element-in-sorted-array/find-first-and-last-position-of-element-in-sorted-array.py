class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums) - 1
        lowest=-1
        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                lowest= mid
                high=mid-1
        low = 0
        high = len(nums) - 1
        highest = -1
        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                highest= mid
                low=mid+1

        return [lowest,highest]