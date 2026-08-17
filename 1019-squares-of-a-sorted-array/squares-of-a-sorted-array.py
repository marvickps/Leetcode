class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lenth = len(nums)
        re= [0] * lenth
        l = 0
        r = lenth-1
        last_index = r
        while l<=r:
            ln = abs(nums[l])
            rn = abs(nums[r])
            if ln > rn:
                re[last_index] = ln**2
                l +=1
            else:
                re[last_index] = rn**2
                r -=1

            last_index -=1
        return re
            

                

