# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cur_level_nodes = [root]
        next_level_nodes = []
        ans = []
        while cur_level_nodes:
            ans.append([])
            for node in cur_level_nodes:
                ans[-1].append(node.val)
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            cur_level_nodes = next_level_nodes
            next_level_nodes = []
        return ans