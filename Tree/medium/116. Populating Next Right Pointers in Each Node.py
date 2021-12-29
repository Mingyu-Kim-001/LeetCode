"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        bfs = deque([root])
        while bfs:
            next_bfs = deque()
            while bfs:
                node = bfs.popleft()
                node.next = bfs[0] if bfs else None
                if node.right:
                    next_bfs.append(node.left)
                    next_bfs.append(node.right)
            bfs = next_bfs
        
        return root