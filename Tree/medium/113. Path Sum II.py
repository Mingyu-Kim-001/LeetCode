# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        if not root:
            return []
        
        def DFS(node, target):
            if not node.left and not node.right:
                return [[node.val]] if node.val == target else []
            left_routes = []
            right_routes = []
            if node.left:
                left_routes = DFS(node.left, target - node.val)
                if left_routes:
                    left_routes = [[node.val]+route for route in left_routes]
            if node.right:
                right_routes = DFS(node.right, target - node.val)
                if right_routes:
                    right_routes = [[node.val]+route for route in right_routes]
            return left_routes + right_routes
        
        return DFS(root, targetSum)