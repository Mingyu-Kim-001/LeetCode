# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        result = None
        def traverse(root):
            nonlocal result
            if not root: return
            if root.val==target.val:
                result = root
                return
            if not result:
                traverse(root.right)
                traverse(root.left)
        traverse(cloned)
        return result