# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        nodes1 = []
        nodes2 = []
        def inorder(node, nodes):
            if not node:
                return
            inorder(node.left, nodes)
            nodes.append(node.val)
            inorder(node.right, nodes)
        
        inorder(root1, nodes1)
        inorder(root2, nodes2)
        i = j = 0
        while i < len(nodes1) and j < len(nodes2):
            if nodes1[i] < nodes2[j]:
                ans.append(nodes1[i])
                i += 1
            else:
                ans.append(nodes2[j])
                j += 1
        while i < len(nodes1):
            ans.append(nodes1[i])
            i += 1
        while j < len(nodes2):
            ans.append(nodes2[j])
            j += 1
        
        return ans