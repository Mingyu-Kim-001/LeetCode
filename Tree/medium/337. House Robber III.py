# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dp = {}
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root in self.dp:
            return self.dp[root]
        money_if_rob_root = root.val
        if root.left:
            money_if_rob_root += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            money_if_rob_root += self.rob(root.right.left) + self.rob(root.right.right)
        money_if_not_rob_root = self.rob(root.left) + self.rob(root.right)
        self.dp[root] = max(money_if_rob_root,money_if_not_rob_root)
        return self.dp[root]