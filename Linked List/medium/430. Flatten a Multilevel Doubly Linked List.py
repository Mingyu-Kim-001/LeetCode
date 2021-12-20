"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        def DFS(head):
            node = head
            while True:
                if node.child:
                    new_next, end = DFS(node.child)
                    old_next = node.next
                    node.next = new_next
                    new_next.prev = node
                    end.next = old_next
                    if old_next:
                        old_next.prev = end
                    node.child = None
                    
                if not node.next:
                    break
                node = node.next
            return head, node
        
        return DFS(head)[0]