# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = 0
        left = root
        while left:
            left = left.left
            max_depth += 1
        max_leaf = 1 << (max_depth - 1)
        
        def get_depth(leaf_num, cur_max_depth, node):
            if cur_max_depth == 1:
                if node:
                    return 1
                return 0
            half = (1 << (cur_max_depth - 2))
            if leaf_num >= half:
                return 1 + get_depth(leaf_num - half, cur_max_depth - 1, node.right)
            else:
                return 1 + get_depth(leaf_num, cur_max_depth - 1, node.left)
        
        l, r = 0, max_leaf
        
        while l < r:
            m = (l + r) // 2
            if l == m:
                break
            if get_depth(m, max_depth, root) == max_depth:
                l = m 
            else:
                r = m
        return max_leaf + l
            