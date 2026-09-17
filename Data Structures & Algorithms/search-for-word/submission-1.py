class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, char, dupe):
            if not char:
                return True

            direction = [[1,0],[-1,0],[0,1],[0,-1]]


            for dir in direction:
                tempX = i + dir[0]
                tempY = j + dir[1]
                if tempX >= 0 and tempX < len(board) and tempY >= 0 and tempY < len(board[0]):
                    if (tempX, tempY) not in dupe:
                        if board[tempX][tempY] == char[0]:
                            if len(char) == 1:
                                return True
                            dupe.add((tempX, tempY))
                            if dfs(tempX, tempY,char[1:], dupe):
                                return True
                            dupe.remove((tempX, tempY))
            return False
                    




        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, word[1:], set()):
                        return True
        return False
                
            
        