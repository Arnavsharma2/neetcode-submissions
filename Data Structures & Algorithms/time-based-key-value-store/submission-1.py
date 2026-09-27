class TimeMap:

    def __init__(self):
        self.timeDict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeDict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        timeList = self.timeDict[key]
        
        l = 0
        r = len(timeList) -1
        res = (float('-inf'), "")
        while l <= r:
            m = (r-l)//2 + l

            if timeList[m][0] <= timestamp:
                if timeList[m][0] > res[0]:
                    res = timeList[m]
            if timestamp > timeList[m][0]:
                l = m + 1
            else:
                r = m - 1
        return res[1]


        
