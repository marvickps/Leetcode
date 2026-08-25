class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        l = len(nums)

        for i in range(l):
            if nums[i] in count:
                count[nums[i]]+=1
            else:
                count[nums[i]] = 1
        
        result = sorted(count, key=count.get, reverse=True)[:k]
        return result