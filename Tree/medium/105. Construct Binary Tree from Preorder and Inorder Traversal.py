# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Time: O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(preorder_R,inorder):
            if not preorder_R or not inorder:return None
            val = preorder_R.pop()
            ind = inorder.index(val)
            node = TreeNode(val=val)
            node.left = helper(preorder_R,inorder[:ind])
            node.right = helper(preorder_R,inorder[ind+1:])
            return node
        return helper(preorder[::-1],inorder)