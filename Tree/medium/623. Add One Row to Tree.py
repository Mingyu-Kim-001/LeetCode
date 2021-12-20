# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        
        if d == 1:
            new_root = TreeNode(val=v,left=root)
            return new_root
        
        def DFS(node,depth):
            if not node: return
            if depth == d - 1:
                new_left = TreeNode(val=v,left=node.left)
                new_right = TreeNode(val=v,right=node.right)
                node.left = new_left
                node.right = new_right
                return
            DFS(node.left,depth+1)
            DFS(node.right,depth+1)
        
        DFS(root,1)
        return root