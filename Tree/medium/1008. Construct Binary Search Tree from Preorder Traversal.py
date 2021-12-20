# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        l, r = 0, len(preorder) - 1 # left limit, rigth limit
        
        def DFS(idx, l, r):
            if l > r:
                return None, idx
            node = TreeNode(preorder[idx])
            i = l
            while i <= r:
                if preorder[i] > preorder[idx]:
                    break
                i += 1
            idx += 1
            node.left, idx = DFS(idx, l + 1, i - 1)
            node.right, idx = DFS(idx, i, r)
            return node, idx
        return DFS(0, l, r)[0]