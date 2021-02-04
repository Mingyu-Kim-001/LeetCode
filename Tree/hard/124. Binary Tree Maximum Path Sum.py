# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Time: O(n)
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        result = float("-inf")
        #result tracks the maximum path sum of the subtree of which head is 'node'.
        #DFS returns the maximum path sum that starts with 'node' and goes downside. 
        def DFS(node):
            if not node: return 0
            nonlocal result
            leftMax = max(DFS(node.left),0)
            rightMax = max(DFS(node.right),0)
            result = max(result,leftMax+rightMax+node.val)
            return max(leftMax,rightMax) + node.val
        DFS(root)
        return result