class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #[-4,-1,-1,0,1,2]
             #l        r -> [-1,-1,2]
                #l     r -> 3>2
                #l    r -> 
        nums = sorted(nums)
        le =len(nums)
        result = []
        for i in range(le):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i+1
            r = le-1
            
            while l<r:

                current = nums[l] + nums[r]
                if current >  -nums[i]:
                    r -= 1
                elif current <  -nums[i]:
                    l += 1
                else:
                    result.append([nums[l], nums[r], nums[i]])
                    l +=1
                    r -=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return result
