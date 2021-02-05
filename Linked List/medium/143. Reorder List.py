# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Time: O(n)
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        i = 0
        nodeDic = {}
        while head:
            nodeDic[i] = head
            head = head.next
            nodeDic[i].next = None
            i+=1
            
        l = 0
        r = i-1
        while l<r:
            nodeDic[l].next = nodeDic[r]
            if l+1<r: 
                nodeDic[r].next = nodeDic[l+1]
            else:
                nodeDic[r].next = None
            l+=1
            r-=1