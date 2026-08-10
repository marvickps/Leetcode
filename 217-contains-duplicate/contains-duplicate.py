class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i, num in enumerate(nums):
        #     if num in nums[i+1::]:
        #         return True 
        # return False

        stored = set()
        for num in nums:
            if num in stored:
                return True
            stored.add(num)
        return False
        