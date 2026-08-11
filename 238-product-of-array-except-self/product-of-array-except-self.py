class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #nums - answer
        #[1,2,3,4]
        #[1,2,6,24] PREFIX
        #[4,12,24,24]POSTFIX
        #[1*24,1*12,2*4,6*1]

        #[1,1,2,6]

        out_list = []
        pre = 1

        for i, n in enumerate(nums): 
            out_list.append(pre)
            pre=pre*n
        post = 1
        for i in range(len(nums)-1,-1,-1):
            out_list[i] = out_list[i]*post
            post=post*nums[i]
        return out_list
            

            
        