class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #[18,6,11,17]
        #h=7

        minimum_k = 1
        max_k = max(piles)

        if h == len(piles):
            return max_k
        
        while minimum_k <= max_k:
            mid = (minimum_k + max_k) //2 #8
            hours = 0
            for pile in piles:
                hours = hours +math.ceil(pile / mid)  #9
                #18/8 - 3
                #6/8 - 1
                #11/8 - 2
                #17 - 3
            
            if hours > h:
                minimum_k = mid + 1
            else:
                max_k = mid -1
        return minimum_k


            
            
            

            



        