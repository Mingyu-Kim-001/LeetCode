# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_dummy = ListNode()
        ge_dummy = ListNode()
        less_cur = less_dummy
        ge_cur = ge_dummy
        cur = head
        while cur:
            if cur.val < x:
                less_cur.next = cur
                less_cur = cur
            else:
                ge_cur.next = cur
                ge_cur = cur
            cur = cur.next
        less_cur.next = ge_dummy.next
        ge_cur.next = None
        return less_dummy.next