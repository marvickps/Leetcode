class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        temp={}
        for i in range(len(nums)):
            if nums[i] in temp:
                temp[nums[i]]+=1
            else:
                temp[nums[i]]=1
        for key,value in temp.items():
            if value==1:
                return key
        

        
        