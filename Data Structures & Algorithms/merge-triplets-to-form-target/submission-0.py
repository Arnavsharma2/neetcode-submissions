class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        set1 = set()
        set2 = set()
        set3 = set()
        notIn = False
        for triplet in triplets:
            for i in range(len(triplet)):
                if triplet[i] > target[i]:
                    notIn = True
            if not notIn:
                set1.add(triplet[0])
                set2.add(triplet[1])
                set3.add(triplet[2])
            
        return target[0] in set1 and target[1] in set2 and target[2] in set3
            
            
