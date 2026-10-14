class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        curr = []
        n = len(s)
        #abcaa
        #[a,b,c,a,a], [a,b,c,aa]
        def backtracking(index_s):
                if index_s == n:
                    res.append(curr.copy())
                    return

                for i in range(index_s + 1, n + 1): #
                    word = s[index_s:i] #0-1 , 0-2, 0-3, 0-4, 0-5
                    
                    if word ==word[::-1]:
                        curr.append(word)
                        backtracking(i)
                        curr.pop()
                


                
        backtracking(0)

        return res
