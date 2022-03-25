# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        nodes = [head]
        table = [0]
        j = 0
        cur = head.next
        while cur:
            nodes.append(cur)
            while j > 0 and nodes[j].val != cur.val:
                j = table[j-1]
            j += nodes[j].val == cur.val
            table.append(j)
            cur = cur.next
            
        def DFS(nodes, table, j, tree_node):
            if not tree_node:
                return False
            while j > 0 and nodes[j].val != tree_node.val:
                j = table[j-1]
            j += nodes[j].val == tree_node.val
            return j == len(nodes) or DFS(nodes, table, j, tree_node.left) or DFS(nodes, table, j, tree_node.right)
        
        return DFS(nodes, table, 0, root)
                