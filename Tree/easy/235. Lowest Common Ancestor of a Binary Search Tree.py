# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Time: O(n)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def DFS(node):
            if p.val<=node.val<=q.val or q.val<=node.val<=p.val: return node
            if p.val<node.val and q.val<node.val: return DFS(node.left)
            if p.val>node.val and q.val>node.val: return DFS(node.right)
        return DFS(root)