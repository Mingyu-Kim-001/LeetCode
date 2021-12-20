"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def DFS(node,ans):
            if not node:
                return
            ans.append(node.val)
            for child in node.children:
                DFS(child,ans)
        DFS(root,ans)
        return ans
            