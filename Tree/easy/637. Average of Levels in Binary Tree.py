# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        bfs = deque([])
        bfs.append([root,0])
        prev_level = sum_on_level = length_on_level = 0
        result = []
        while bfs:
            node,level = bfs.popleft()
            if not node:
                continue
            if level == prev_level :
                sum_on_level += node.val
                length_on_level += 1
            else:
                result.append(sum_on_level/length_on_level)
                sum_on_level = node.val
                length_on_level = 1
                prev_level = level
            bfs.append([node.left,level+1])
            bfs.append([node.right,level+1])
        result.append(sum_on_level/length_on_level)
        return result