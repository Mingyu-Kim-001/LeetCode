# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = None
        
        def DFS(node):
            if not node:
                return 0
            nonlocal result
            left = DFS(node.left)
            right = DFS(node.right)
            
            if node == p or node == q:
                if left or right:
                    result = node
                else:
                    return 1
            elif left + right == 2:
                result = node
                return -1
            return left + right
        
        DFS(root)
        return result