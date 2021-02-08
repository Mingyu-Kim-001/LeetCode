# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0
        def traverse(node,parent,grandparent):
            nonlocal total
            if node==None: return
            if grandparent and grandparent.val%2==0: total+=node.val
            traverse(node.right,node,parent)
            traverse(node.left,node,parent)
        traverse(root,None,None)
        return total