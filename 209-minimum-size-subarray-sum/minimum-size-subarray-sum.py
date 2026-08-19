class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        r = 0
        minn = len(nums) + 1
        summ = 0

        while r < len(nums) or summ >= target:

            if summ < target:
                summ += nums[r]
                r += 1

            else:
                minn = min(minn, r - l)

                summ -= nums[l]
                l += 1

        if minn == len(nums) + 1:
            return 0

        return minn