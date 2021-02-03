# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Time: O(n)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def DFS(nodeP,nodeQ):
            if not nodeP or not nodeQ:
                return not nodeP and not nodeQ
            if nodeP.val!=nodeQ.val: return False
            return DFS(nodeP.left,nodeQ.left) and DFS(nodeP.right,nodeQ.right)
        return DFS(p,q)