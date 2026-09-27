class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        for course in prerequisites:
            prereq[course[0]].append(course[1])

        visited = set()
        def dfs(i):
            if i in visited:
                return False
            visited.add(i)

            if i in prereq:
                for num in prereq[i]:
                    return dfs(num)
            else:
                return True
            

        
        res = []
        for i in range(numCourses):
            visited.clear()
            if dfs(i):
                res.append(i)
            else:
                return []
        
        return res if len(res) == numCourses else []

        
        
