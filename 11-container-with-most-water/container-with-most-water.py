class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        left= 0
        right = len(height)-1
        while (left<right):
            temp = 0
            index_diff = right - left #8-0,

            if height[left] >= height[right]: # 1 >? 7
                temp = height[right] * index_diff
                right -=1
            
            else:
                temp = height[left] * index_diff #
                left += 1
            if temp > max:
                max = temp

        return max
                