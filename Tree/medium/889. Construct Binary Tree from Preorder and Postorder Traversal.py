# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.preIdx = self.postIdx = 0
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        root = TreeNode(val=pre[self.preIdx])
        self.preIdx+=1
        if root.val!=post[self.postIdx]:
            root.left = self.constructFromPrePost(pre,post)
        if root.val!=post[self.postIdx]:
            root.right = self.constructFromPrePost(pre,post)
        self.postIdx+=1
        return root