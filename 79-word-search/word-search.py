class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        #[A,B,C,E]
        #[S,F,C,S]
        #[A,D,E,E]

        #ABCCED
        
        row = len(board)
        col = len(board[0])

        last_visited = set()
        def backtracking(i,r,c):
            if i == len(word):
                return True
            
            #unbound:
            unbound = r<0 or r >= row or c <0 or c>=col

            if (unbound or
                board[r][c] !=word[i] or
                (r,c) in last_visited
                ):
                return False

            last_visited.add((r,c))

            res = (
                backtracking(i+1,r+1,c) or
                backtracking(i+1,r,c+1) or
                backtracking(i+1,r-1,c) or
                backtracking(i+1,r,c-1)
            )
            last_visited.remove((r,c))

            return res
        
        for r in range(row):
            for c in range(col):
                if backtracking(0,r,c):
                    return True
        return False
        




