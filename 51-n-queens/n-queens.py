class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        #queen = [] list of index
        def backtracking(row, queen):
            if len(queen) == n:
                res_board = []
                for col in queen:
                    res_board.append("."*col+"Q"+"."*(n-col-1))
                res.append(res_board)
                return

            for col in range(n):
                if isSafe(queen, row, col):
                    queen.append(col)
                    backtracking(row+1,queen)
                    queen.pop()
            
        def isSafe(queen,row, col):
            for r, queen_col_index in enumerate(queen):
                if queen_col_index == col or abs(queen_col_index - col) == row - r:
                    return False
            return True


        backtracking(0,[])
        
        return res