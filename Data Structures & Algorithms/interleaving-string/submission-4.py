class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) > len(s3):
            return False

        failed = {}
        def backtracking(i, j):
            k = i + j
            if k == len(s3):
                return True

            if i < len(s1) and s1[i] == s3[k] and (i+1, j) not in failed:
                if backtracking(i+1, j) :
                    return True
                else:
                    failed[(i + 1, j)] = True

            if j < len(s2) and s2[j] == s3[k] and (i, j+1) not in failed:
                if backtracking(i, j+1):
                    return True
                else:
                    return False

            return False
    
        return backtracking(0, 0)
                    

