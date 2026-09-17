class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            visited.add((r, c))
            bounds = [[0,1],[0,-1],[1,0],[-1,0]]
            
            for bound in bounds:
                moveR = r + bound[0]
                moveC = c + bound[1]
                if moveR < 0 or moveC < 0 or moveR > len(heights)-1 or moveC > len(heights[0])-1:
                    continue
                if heights[moveR][moveC] >= heights[r][c]:
                    dfs(moveR, moveC, visited)


        for r in range(len(heights)):
            dfs(r, 0, pacific)
            dfs(r, len(heights[0])-1, atlantic)
        for c in range(len(heights[0])):
            dfs(0, c, pacific)
            dfs(len(heights)-1, c, atlantic)
        
        res = []
        for pair in pacific:
            if pair in atlantic:
                res.append([pair[0], pair[1]])
        return res
            
        




        
