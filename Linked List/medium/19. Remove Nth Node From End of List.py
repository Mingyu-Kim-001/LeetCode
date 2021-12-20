# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Time: O(n). Especially, only one pass
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(next=head)
        nPrev = dummy
        nPrevPrev = dummy
        count = 0
        while head:
            count+=1
            if count>=n:
                nPrev = nPrev.next
                if count>n: nPrevPrev = nPrevPrev.next
            head = head.next
        nPrevPrev.next = nPrev.next
        return dummy.next