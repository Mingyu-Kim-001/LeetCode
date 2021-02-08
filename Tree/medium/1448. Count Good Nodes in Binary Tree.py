# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        def DFS(node,maxValue):
            if not node:return
            nonlocal result
            if node.val>=maxValue:
                result+=1
                DFS(node.left,node.val)
                DFS(node.right,node.val)
            else:
                DFS(node.left,maxValue)
                DFS(node.right,maxValue)
        DFS(root,root.val)
        return result
            