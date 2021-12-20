# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def inorder_reverse(node,curSum):
            if not node: return curSum
            curSum = inorder_reverse(node.right,curSum)
            curSum+=node.val
            node.val = curSum
            curSum = inorder_reverse(node.left,curSum)
            return curSum
        inorder_reverse(root,0)
        return root