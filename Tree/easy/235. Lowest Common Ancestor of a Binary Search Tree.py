# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(n)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def DFS(root,p,q):
            if p.val<=root.val<=q.val or q.val<=root.val<=p.val:
                return root
            if p.val<root.val and q.val<root.val:
                return DFS(root.left,p,q)
            if p.val>root.val and q.val>root.val:
                return DFS(root.right,p,q)
            
        return DFS(root,p,q)