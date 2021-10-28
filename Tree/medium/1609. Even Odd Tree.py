# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        cur_level_nodes = [root]
        level = 0
        next_level_nodes = []
        while cur_level_nodes:
            for i, node in enumerate(cur_level_nodes):
                if (node.val + level) % 2 == 0:
                    return False
                if level % 2 == 0 and i > 0 and cur_level_nodes[i-1].val >= node.val:
                    return False
                if level % 2 == 1 and i > 0 and cur_level_nodes[i-1].val <= node.val:
                    return False
                
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            
            level += 1
            cur_level_nodes = next_level_nodes
            next_level_nodes = []
            
        return True