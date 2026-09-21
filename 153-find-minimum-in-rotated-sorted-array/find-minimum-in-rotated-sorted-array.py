class Solution:
    def findMin(self, nums: list[int]) -> int:
        #n - 1,2,3,4,5
        #          m     r
        #3, 1, 2

        r = len(nums)-1
        l = 0
        while l< r:
            mid = (l+r)//2

            if nums[mid]>nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
            
