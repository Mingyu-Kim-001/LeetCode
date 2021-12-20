# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def DFS(prev_sum, node):
            if not node.left and not node.right:
                return prev_sum * 10 + node.val
            if not node.left:
                return DFS(prev_sum * 10 + node.val, node.right)
            if not node.right:
                return DFS(prev_sum * 10 + node.val, node.left)
            return DFS(prev_sum * 10 + node.val, node.right) + DFS(prev_sum * 10 + node.val, node.left)
            
        return DFS(0, root)