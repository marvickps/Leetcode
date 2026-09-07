class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #[23,2,4,6,7]
        #good - if len > 2 and sum % k == 0

        # index:       0   1   2   3   4
        # nums:       23   2   4   6   7
        # prefix:     23  25  29  35  42
        # remainder:   5   1   5   5   0

        reminder = 0
        sums = 0
        saw = {}

        for i in range(len(nums)):
            sums = sums + nums[i]
            reminder = sums % k

            if reminder == 0 and i >= 1:
                return True

            if reminder in saw:
                if i - saw[reminder]>=2:
                    return True
            else:
                saw[reminder] = i
            
        return False

                     




