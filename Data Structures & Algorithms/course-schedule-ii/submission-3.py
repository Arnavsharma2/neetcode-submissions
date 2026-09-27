class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        for course in prerequisites:
            prereq[course[0]].append(course[1])

        res = []
        self.res = res

        visited = set()
        completed = set()
        res = []
        def dfs(i):
            if i in visited:
                return False
            visited.add(i)

            for num in prereq[i]:
                if not dfs(num):
                    return False

            if i not in completed:
                res.append(i)
                completed.add(i)

            return True
    
        for i in range(numCourses):
            visited.clear()
            if not dfs(i):
                return []
        print(res)
        return res if len(res) == numCourses else []

        
        
