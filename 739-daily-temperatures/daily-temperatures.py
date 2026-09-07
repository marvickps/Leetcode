class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #[73,74,75,71,69,72,76,73]
        #[1 , 1, 4, 3, 1, 1, 0, 0]
        #[6]

        result = [0] * len(temperatures)
        stk = []

        for i, temp in enumerate(temperatures):
            while stk and temp>temperatures[stk[-1]]:
                diff = stk.pop()
                result[diff] = i - diff
            
            stk.append(i)

        return result 



    