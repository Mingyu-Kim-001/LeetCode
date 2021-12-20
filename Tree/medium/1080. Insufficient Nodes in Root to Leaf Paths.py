# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def DFS(node,partSum):
            if not node.left and not node.right:
                return partSum+node.val>=limit
            left = right = False
            if node.left:
                left = DFS(node.left,partSum+node.val)
            if node.right:
                right = DFS(node.right,partSum+node.val)
            if not left:
                node.left = None
            if not right:
                node.right = None
            
            return left or right
        if not DFS(root,0): return None
        return root