class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        #[1,2,3]-[1,3,2]
        res = []
        curr_path = []

        def backtrack(temp_list):
            if len(temp_list) == 0:
                res.append(curr_path.copy())
                return
            
            #Explore
            for i in range(len(temp_list)):
                curr_path.append(temp_list[i])
                backtrack(temp_list[:i]+temp_list[i+1:])
                curr_path.pop()

        backtrack(nums)
        return res


