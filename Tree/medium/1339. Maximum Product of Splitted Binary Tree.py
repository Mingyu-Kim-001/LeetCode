# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def get_sum(node):
            if not node:
                return 0
            return node.val + get_sum(node.left) + get_sum(node.right)
        
        tree_sum = get_sum(root)
        half_tree_sum = tree_sum / 2
        
        def get_close(node):
            if not node:
                return 0, 0
            left_sum, left_close = get_close(node.left)
            right_sum, right_close = get_close(node.right)
            
            return node.val + left_sum + right_sum, min(left_close, right_close, node.val + left_sum + right_sum, key=lambda x:abs(x-half_tree_sum))
        
        return get_close(root)[1] * (tree_sum - get_close(root)[1]) % (pow(10,9) + 7)