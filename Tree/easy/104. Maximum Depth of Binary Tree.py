# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Time: O(n)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def DFS(node):
            if not node: return 0
            return 1 + max(DFS(node.left),DFS(node.right))
        return DFS(root)