class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #[73,74,75,71,69,72,76,73]
        # l   r
        n = len(temperatures)
        ans = [0]*n
        stack = [] #0
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp: # 73<74
                j = stack.pop()
                ans[j] = i -j
            
            stack.append(i)
        return ans