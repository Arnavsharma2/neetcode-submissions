class WordDictionary:

    def __init__(self):
        self.hashNest = {}

    def addWord(self, word: str) -> None:
        root = self.hashNest
        for char in word:
            if not char in self.hashNest:
                self.hashNest[char] = {}
            
            self.hashNest = self.hashNest[char]
        self.hashNest['`'] = True
        self.hashNest = root

    def search(self, word: str) -> bool:

        def dfs(curr, i):
            if i == len(word):
                return '`' in curr

            if word[i] != '.':
                if word[i] not in curr:
                    return False
                return dfs(curr[word[i]], i + 1)

            for key in curr:
                if key == '`':
                    continue

                if dfs(curr[key], i + 1):
                    return True
                
            return False

        return dfs(self.hashNest, 0)




        
