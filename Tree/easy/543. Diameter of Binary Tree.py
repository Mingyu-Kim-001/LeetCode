# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        result = 0
                
        def DFS(node):
            if not node:
                return 0
            left = DFS(node.left)
            right = DFS(node.right)
            nonlocal result
            result = max(result,left+right)
            return max(left,right) + 1
        
        DFS(root)
        return result