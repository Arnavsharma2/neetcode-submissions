# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        middle = head
        last = head.next
        while last and last.next:
            middle = middle.next
            last = last.next.next
        
        temp = middle.next
        middle.next = None
        middle = temp
        
        prev = None
        while middle:
            temp = middle.next
            middle.next = prev
            prev = middle
            middle = temp
        
        middle = prev
        
        while middle:
            temp = head.next 
            head.next = middle 
            middle = middle.next 
            head.next.next = temp
            head = temp 
            

