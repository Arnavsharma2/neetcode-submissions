# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        scout = head

        for i in range(n):
            scout = scout.next
        
        while scout:
            scout = scout.next
            prev = prev.next
        
        prev.next = prev.next.next
        return dummy.next
        
        
        