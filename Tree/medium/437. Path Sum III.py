# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        result = 0
        
        def DFS(node,prefix):
            if not node:
                return
            prefix += node.val
            nonlocal result
            result += dp[prefix-target] if prefix - target in dp else 0
            dp[prefix] += 1
            DFS(node.left,prefix)
            DFS(node.right,prefix)
            dp[prefix] -= 1
            if not dp[prefix]:
                dp.pop(prefix,None)
                
        DFS(root,0)    
        return result