# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generateWithList(nums:List[int]) -> List[Optional[TreeNode]]:
            if not nums:
                return [None]
            if len(nums) == 1:
                return [TreeNode(nums[0])]
            ans = []
            for i in range(len(nums)):
                lefts = generateWithList(nums[:i])
                rights = generateWithList(nums[i+1:])
                for left in lefts:
                    for right in rights:
                        ans.append(TreeNode(nums[i],left,right))
            return ans
        return generateWithList(range(1,n+1))
                