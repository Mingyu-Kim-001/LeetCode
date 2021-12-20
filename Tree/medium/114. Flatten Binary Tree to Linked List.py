# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        a = self.flatten(root.right)
        root.right = self.flatten(root.left)
        root.left = None
        end = root
        while end.right:
            end = end.right
        end.right = a
        return root