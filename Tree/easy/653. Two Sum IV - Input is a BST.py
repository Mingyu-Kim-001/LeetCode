# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Time: O(n)
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        valSet = set()
        def DFS(node,valSet):
            if not node:
                return False
            if k-node.val in valSet: return True
            valSet.add(node.val)
            return DFS(node.left,valSet) or DFS(node.right,valSet)
        return DFS(root,valSet)