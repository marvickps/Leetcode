class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #[1,1,2,1,2,3,4,5,3,2,1,2,3,2,1,3,1,2,2,1]
        # L
        #     R
        count = {}
        l =0
        r= 0
        total =0
        result = 0
        while r<len(fruits):
            if fruits[r] in count:
                count[fruits[r]]+=1 
            else:
                count[fruits[r]]=1
            total += 1

            while len(count) > 2: 
                count[fruits[l]]-=1
                total -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l+=1
            if result<total:
                result = total
            r+=1

        return result
            

            
        

                


        