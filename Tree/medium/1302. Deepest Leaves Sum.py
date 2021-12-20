# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        deepest_depth = ans = 0
        def DFS(node,depth):
            if not node:
                return
            nonlocal deepest_depth
            nonlocal ans
            if depth == deepest_depth:
                ans += node.val
            elif depth > deepest_depth:
                deepest_depth = depth
                ans = node.val
            DFS(node.left,depth+1)
            DFS(node.right,depth+1)
        DFS(root,1)
        return ans
            