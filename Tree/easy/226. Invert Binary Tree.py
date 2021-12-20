# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Time:O(n)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def DFS(node):
            if not node:return
            node.left,node.right = DFS(node.right),DFS(node.left)
            return node
        return DFS(root)