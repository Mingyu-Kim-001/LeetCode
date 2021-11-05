# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def DFS(node, val):
            if not node:
                return 0, 0
            max_l, l = DFS(node.left, node.val)
            max_r, r = DFS(node.right, node.val)
            max_cur = max(max_l, max_r, l + r + 1)
            if node.val == val:
                return max_cur, max(l, r) + 1
            return max_cur, 0
        
        return DFS(root, root.val)[0] - 1