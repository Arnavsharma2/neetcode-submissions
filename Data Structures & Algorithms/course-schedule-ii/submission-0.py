class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        for course in prerequisites:
            prereq[course[0]].append(course[1])

        def dfs(i):
            if i in prereq:
                for num in prereq:
                    return dfs(num)
            else:
                return True
            

        
        res = []
        for i in range(numCourses):
            if dfs(i):
                res.append(i)
            else:
                return []
        
        return res if res == len(numCourses) else []

        
        
