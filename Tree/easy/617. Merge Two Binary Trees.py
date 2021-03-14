# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        
        def DFS(node1,node2):
            if not node1:
                return node2
            if not node2:
                return node1
            left = DFS(node1.left,node2.left)
            right = DFS(node1.right,node2.right)
            new_node = TreeNode(val=node1.val+node2.val,
                                left=left,
                                right=right)
            return new_node
        
        return DFS(root1,root2)