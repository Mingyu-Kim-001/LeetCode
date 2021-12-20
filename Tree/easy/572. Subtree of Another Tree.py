# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def check(a,b):
            if not a and not b: return True
            if not (a and b): return False
            if a.val!=b.val:return False
            return check(a.left,b.left) and check(a.right,b.right)
        
        def DFS(head):
            if not head: return False
            if check(head,t): return True
            return DFS(head.left) or DFS(head.right)
        
        return DFS(s)