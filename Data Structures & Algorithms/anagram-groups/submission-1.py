class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        contained = defaultdict(list)
        for word in strs:
            letters = [0]*26
            for char in word:
                letters[ord(char)-ord('a')] += 1
            letterSet = tuple(letters)
            contained[letterSet].append(word)
        
        res = []
        for key, wordList in contained.items():
            res.append(wordList)
        return res

