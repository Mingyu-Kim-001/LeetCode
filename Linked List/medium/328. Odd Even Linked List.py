# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        even_head = even_prev = head
        odd_head = odd_prev = head.next
        idx = 0
        cur = head.next.next
        while cur:
            if idx % 2 == 0:
                even_prev.next = cur
                even_prev = cur
            else:
                odd_prev.next = cur
                odd_prev = cur
            cur = cur.next
            idx += 1
        
        even_prev.next = odd_head
        odd_prev.next = None
        return head
        