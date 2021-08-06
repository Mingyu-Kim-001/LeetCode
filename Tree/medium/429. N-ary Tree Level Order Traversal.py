"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        bfs = deque()
        bfs.append([root,0])
        prev_depth = 0
        ans = [[]]
        while bfs:
            node, depth = bfs.popleft()
            if depth > prev_depth:
                ans.append([])
                prev_depth = depth
            ans[-1].append(node.val)
            for child in node.children:
                bfs.append([child, depth+1])
        return ans
                
                