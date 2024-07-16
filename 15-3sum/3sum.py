class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        dictMap={}
        retList = []
        temp=0
        for i in range(len(nums)):
            dictMap={}
            for j in range(i+1,len(nums)):
                firstNum = (-nums[i])-nums[j]
                if firstNum in dictMap and ([nums[i],nums[j],firstNum]) not in retList:
                    retList.append([nums[i],nums[j],firstNum])
                    dictMap.pop(firstNum)
                else:
                    dictMap[nums[j]] = firstNum

        return retList
            
        