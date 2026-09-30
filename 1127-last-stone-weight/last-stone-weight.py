class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # heap = []

        #[1,1,2,4,7,8]
        #[2,7,4,1,8,1] -> 
        # stones.sort() # [9,10,1,7,3] - > [1,3,7,9,10]

        heapq.heapify_max(stones) 

        while len(stones)>1:
            y=heapq.heappop_max(stones)#10, 7
            x=heapq.heappop_max(stones)#9,  3

            if x == y:
                continue
            else:
                y =abs(y-x) #1 #4
                heapq.heappush_max(stones,y) #[1,1,3,7], [,1,1]
        if stones:
            return stones[0]
        else: 
            return 0