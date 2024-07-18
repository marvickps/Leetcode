class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        while nums[l]>nums[r]:
            l+=1
        return nums[l]
            

            
        
       
        