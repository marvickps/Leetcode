class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #{100:1,4:}
        count=set(nums)
        re =0 

        for n in count:
            if n-1 not in count:
                temp = 1

                while  n + temp in count:
                    temp += 1

                if temp > re:
                    re = temp


        return re