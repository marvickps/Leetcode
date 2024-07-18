class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)

        l=0
        r=n-1
        while nums[l]>nums[r]:
            l+=1
        return nums[l]
            

            
        
       
        