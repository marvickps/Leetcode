class TrieNode:
    def __init__(self):
        self.levels = {}
        self.isEnd = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.levels:
                node.levels[ch] = TrieNode()
            node = node.levels[ch]

        node.isEnd = True
            

    def search(self, word: str) -> bool:
        node = self.root
        def backtrack(node, temp):
            #base
            if temp == len(word):
                return node.isEnd
            
            ch = word[temp]
            
            #explore
            if ch == ".":
                for each in node.levels.values(): #a,b,c 
                    if backtrack(each,temp+1):
                        return True
                return False
            
            if ch not in node.levels:
                return False
        
            return backtrack(node.levels[ch],temp+1)

        return backtrack(node, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)