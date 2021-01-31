# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Time: O(n), Space: O(n)
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 0
        kth = None
        def inorder(head):
            nonlocal count,kth
            if kth: return
            if head.left: inorder(head.left)
            count+=1
            if count==k: 
                kth = head.val
                return
            if head.right: inorder(head.right)
        inorder(root)
        return kth