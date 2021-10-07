# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        row = []
        row.append(root)
        ans = []
        while row:
            next_row = []
            max_val = float("-inf")
            while row:
                node = row.pop()
                max_val = max(max_val, node.val)
                if node.left:
                    next_row.append(node.left)
                if node.right:
                    next_row.append(node.right)
            ans.append(max_val)
            row = next_row
        return ans