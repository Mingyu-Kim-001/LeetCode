# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def DFS(node):
            if not node:
                return False
            left = DFS(node.left)
            right = DFS(node.right)
            if not left:
                node.left = None
            if not right:
                node.right = None
            return node.val == 1 or left or right
        
        return root if DFS(root) else None