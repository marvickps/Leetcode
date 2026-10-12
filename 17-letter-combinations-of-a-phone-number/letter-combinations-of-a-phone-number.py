class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letters={
            "2":("a","b","c"),
            "3":("d","e","f"),
            "4":("g","h","i"),
            "5":("j","k","l"),
            "6":("m","n","o"),
            "7":("p","q","r","s"),
            "8":("t","u","v"),
            "9":("w","x","y","z")
        }

        res = []
        sub_combo = []
        def backtrack(i):
            if i >= len(digits):
                res.append("".join(sub_combo))
                return

            #include
            for ch in letters[digits[i]]:
                sub_combo.append(ch)
                backtrack(i+1)
                sub_combo.pop()

        backtrack(0)
        return res