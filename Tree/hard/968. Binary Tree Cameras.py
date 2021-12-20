# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
        self.root = None
        
    def DFS(self, node:TreeNode) -> bool:
        
        if not node:
            return True, False
        
        is_left_monitored, left_camera_exists = self.DFS(node.left)
        is_right_monitored, right_camera_exists = self.DFS(node.right)
        
        if not is_left_monitored or not is_right_monitored:
            self.ans += 1
            return True, True
        
        if left_camera_exists or right_camera_exists:
            return True, False
        
        if node == self.root:
            self.ans += 1
        return False, False
            
        
    def minCameraCover(self, root: TreeNode) -> int:
        
        self.root = root
        self.DFS(root)
        return self.ans
            
        
        