class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        def backtracking(i, j):
            k = i + j

            if i < len(s1) and s1[i] == s3[k]:
                if backtracking(i+1, j):
                    return True

            if j < len(s2) and s2[j] == s3[k]:
                if backtracking(i, j+1):
                    return True
                else:
                    return False

            if k == len(s3):
                return True

            return False
    
        return backtracking(0, 0)
                    

