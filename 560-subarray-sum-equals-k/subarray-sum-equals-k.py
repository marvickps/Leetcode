class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #1,1,1 k=2
        res = 0
        curSum = 0
        prefixSums = {}
        for num in nums:
            curSum += num

            if curSum == k:
                res += 1

            if curSum - k in prefixSums:
                res += prefixSums[curSum - k]

            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1

        return res
