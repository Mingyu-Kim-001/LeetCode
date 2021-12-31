# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, parent_max_val, parent_min_val):
        if not node:
            return -1
        cur_max = max(parent_max_val - node.val, node.val - parent_min_val)
        parent_max_val = max(parent_max_val, node.val)
        parent_min_val = min(parent_min_val, node.val)
        return max(cur_max, self.helper(node.left, parent_max_val, parent_min_val), self.helper(node.right, parent_max_val, parent_min_val))
        
    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return max(self.helper(root.left, root.val, root.val), self.helper(root.right, root.val, root.val))