# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def DFS(node, seen, k):
            if not node:
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return DFS(node.left, seen, k) or DFS(node.right, seen, k)
        
        return DFS(root, set(), k)