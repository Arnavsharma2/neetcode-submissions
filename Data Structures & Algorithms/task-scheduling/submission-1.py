class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countDict = {}
        cooldown = {}
        for task in tasks:
            countDict[task] = countDict.get(task, 0) + 1
            cooldown[task] = 0
        
        cycle = 0
        remaining = len(tasks)

        while remaining > 0:
            sortedKeys = [key for key, value in sorted(countDict.items(), key=lambda i: i[1], reverse=True)]
            ranTask = False

            for task in sortedKeys:
                if countDict[task] > 0 and cycle >= cooldown[task]:
                    countDict[task] -= 1
                    cooldown[task] = cycle + n + 1
                    remaining -= 1
                    ranTask = True
                    break
                
            if ranTask:
                cycle += 1
            else:
                cycle = min(cooldown[task] for task in countDict if countDict[task] > 0)
        return cycle
                


