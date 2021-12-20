# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Time: O(n)
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def DFS(node,clonedNode):
            if not node: return
            if node==target:return clonedNode
            left = DFS(node.left,clonedNode.left)
            if left: return left
            right = DFS(node.right,clonedNode.right)
            if right: return right
        return DFS(original,cloned)