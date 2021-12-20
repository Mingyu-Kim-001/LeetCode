# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def DFS(node, max_val):
            if not node:
                return 0
            return int(max_val <= node.val) + DFS(node.left, max(max_val, node.val)) + DFS(node.right, max(max_val, node.val))
        
        return DFS(root, root.val)