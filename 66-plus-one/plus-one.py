class Solution:
    # def rec(self, num: int) -> int:
    def plusOne(self, digits: List[int]) -> List[int]:
        #[1,2,3,9] - if 9 - push one index back 
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits = [1] + digits
            else:
                digits[i]+=1
                break
        return digits
        
