# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''

        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        
        sumVal = int(num1[::-1]) + int(num2[::-1])

        sumStr = str(sumVal)[::-1]



        prev = curr = ListNode(int(sumStr[0]))
        for i in range(1, len(sumStr)):
            curr.next = ListNode(int(sumStr[i]))
            curr = curr.next
        return prev



