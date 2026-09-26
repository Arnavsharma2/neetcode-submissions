class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for i in range(len(position)):
            combined.append((position[i], speed[i]))
        
        combined.sort()
        # [(0,1), (1,2), (4,2), (7,1)]
        # target = 10
        fleets = 0
        times = []

        for i in range(len(combined)-1, -1, -1):
            pos, rate = combined[i]
            times.append((target-pos) / rate)
            if i < len(combined)-1 and times[-2] >= times[-1]:
                times.pop(-1)
            
        print(times)
        
        return len(times)

