class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        i = 0
        j = l -1
        while i <= j:
            mid = (i+j) //2
            if nums[mid] < target:
                i = mid+1
            elif nums[mid] > target:
                j = mid -1
            else:
                return mid
        
        return -1