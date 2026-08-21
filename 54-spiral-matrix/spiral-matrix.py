class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #[[1,2,x,3],
        # [4,5,y,6],
        # [e,2,y,6],
        # [f,2,y,6],
        # [7,8,z,9]]
        if matrix == []:
            return []

        res = []
        m = len(matrix)
        n = len(matrix[0])
        top, bottom = 0, m-1 #1
        left, right = 0, n-1

        while top <= bottom and left <= right:
            # R
            for col in range(left, right + 1): 
                res.append(matrix[top][col]) #1,2,X,3
            top += 1
            # C
            for row in range(top,bottom+1):
                res.append(matrix[row][right])
            right -= 1
            if top <= bottom:
               #R (reverse)
                for col in range(right, left-1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            if left <= right:
                #C (reverse)
                for row in range(bottom,top-1,-1):
                    res.append(matrix[row][left])
                left += 1
        return res
        