# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Time: O(n)
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        curLeaf = [root]
        result = [[root.val]]
        while True:
            temp = []
            for node in curLeaf:
                if node.left: 
                    temp.append(node.left)
                if node.right: 
                    temp.append(node.right)
            if temp:
                result.append([node.val for node in temp])
                curLeaf = temp
            else:
                break
        return result