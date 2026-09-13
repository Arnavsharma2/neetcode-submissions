# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode()
        prev.next = head
        scout = head

        for i in range(n):
            scout = scout.next
        
        while scout and scout.next:
            scout = scout.next
            prev = prev.next
        
        if scout:
            prev = prev.next
            prev.next = scout
        else:
            prev.next = scout
            return prev.next
        return head
        
        
        