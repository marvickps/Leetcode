class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]] = 1
        returnlist = []
        for k, v in d.items():
            if v == 2:
                returnlist.append(k)
        return returnlist