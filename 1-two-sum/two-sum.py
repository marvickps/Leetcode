class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums #target
        # h={}
        # for i, num in enumerate(nums):
        #     diff = target - num
        #     if diff in h:
        #         return [h[diff],i]
        #     h[num] = i

        hex = {}                       
        for i in range(len(nums)): 
            l = target - nums[i] #13-2 , 13-4
            if l in hex:
                return [hex[l],i]
            hex[nums[i]] = i



        


            
