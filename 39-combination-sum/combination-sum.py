class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        #2-2-2-3>8
        #2-2-3 = 8 
        res = []
        support_list = []
        def backtracking(start):
            if sum(support_list) == target:
                res.append(support_list.copy())
                return
            if sum(support_list)>target:
                return

            for i in range(start, len(candidates)):
                support_list.append(candidates[i])
                backtracking(i)
                support_list.pop()
            
            
        backtracking(0)
        return res
            
            
