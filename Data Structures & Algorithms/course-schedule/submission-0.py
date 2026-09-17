class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        path = set()
        def dfs(course):
            if course in path:
                return False
            if preMap[course] == []:
                return True
            
            path.add(course)

            for c in preMap[course]:
                if dfs(c) == False:
                    return False
            
            path.remove(course)
            return True
            

                    
            
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

