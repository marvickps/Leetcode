class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        curr = []

        def backtracking(start):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            
            if sum(curr)>target:
                return
            
            for i in range(start, len(candidates)): #0,1,2
                if i != start and candidates[i] == candidates[i-1]: #1(1) - 2(1)
                    continue
                curr.append(candidates[i])
                backtracking(i+1) #0,
                curr.pop()



        backtracking(0)
        return res