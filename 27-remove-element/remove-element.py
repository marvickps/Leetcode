class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        v = 0
        while v <= len(nums)-1:
            if nums[v] == val:
                nums.remove(val)
                continue
            v += 1
        return len(nums)
        