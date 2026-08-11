class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l= len(nums)-1
        i = 0
        while i < l :
            if nums[i] == 0:
                nums.append(nums[i])
                nums.pop(i)
                l = l-1
            else: 
                i = i+1

        return nums