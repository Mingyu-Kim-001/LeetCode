# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        result = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)
        answer = float("inf")
        for i in range(len(result)-1):
            answer = min(answer,result[i+1]-result[i])
        return answer