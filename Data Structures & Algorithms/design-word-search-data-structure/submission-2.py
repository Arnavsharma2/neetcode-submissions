class WordDictionary:

    def __init__(self):
        self.hashStore = {}

    def addWord(self, word: str) -> None:
        root = self.hashStore
        for char in word:
            if char not in self.hashStore:
                self.hashStore[char] = {}
            
            self.hashStore = self.hashStore[char]
        self.hashStore["`"] = True
        self.hashStore = root


    def search(self, word: str) -> bool:

        def dfs(curr, i):
            if len(word) == i:
                return '`' in curr
            
            if word[i] == '.':
                for letter in curr:
                    if letter == '`':
                        continue
                    
                    if dfs(curr[letter], i + 1):
                        return True
                return False
            else:
                if word[i] not in curr:
                    return False
                return dfs(curr[word[i]], i + 1)
            
        return dfs(self.hashStore, 0)





        
