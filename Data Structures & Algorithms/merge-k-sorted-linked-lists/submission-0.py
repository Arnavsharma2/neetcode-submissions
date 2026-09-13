# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        i = 0
        while len(lists)> 1:
            merged = []
            for i in range(0, len(lists), 2):
                first = lists[i]
                second = lists[i+1] if i + 1 < len(lists) else None
                merged.append(self.mergeList(first, second))
            lists = merged

        if lists:
            return lists[0]
        else:
            return None
            

    def mergeList(self, first, second):
            dummy = ListNode()
            node = dummy
            while first and second:
                if first.val > second.val:
                    node.next = second
                    second = second.next
                    node = node.next
                else:
                    node.next = first
                    first = first.next
                    node = node.next
            node.next = first or second
            return dummy.next
            



