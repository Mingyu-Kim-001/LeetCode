# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Time: O(n)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def DFS(node,maxVal):
            if not node: return 0
            count = 0
            if maxVal<=node.val:
                maxVal = node.val
                count = 1
            return count + DFS(node.left,maxVal) + DFS(node.right,maxVal)
        return DFS(root,float("-inf"))