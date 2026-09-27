"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        visited = {}
        dummy = prev = Node(0)
        while head:
            if head in visited:
                prev.next = visited[head]
            else:
                visited[head] = Node(head.val)
                prev.next = visited[head]
            if head.random:
                if head.random in visited:
                    prev.next.random = visited[head.random]
                else:
                    visited[head.random] = Node(head.random.val)
                    prev.next.random = visited[head.random]
            prev = prev.next
            head = head.next
        return dummy.next
