class PrefixTree:

    def __init__(self):
        self.words = set()
        self.hashNest = {}

    def insert(self, word: str) -> None:
        self.words.add(word) 
        root = self.hashNest
        for char in word:
            if char not in self.hashNest:
                self.hashNest[char] = {}
            
            self.hashNest = self.hashNest[char]
        self.hashNest = root
            


    def search(self, word: str) -> bool:
        return word in self.words
        

    def startsWith(self, prefix: str) -> bool:
        root = self.hashNest
        for char in prefix:
            if char not in self.hashNest:
                return False
            self.hashNest = self.hashNest[char]
        self.hashNest = root
        return True
        
        