# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n = 0
        node = head
        while node:
            node = node.next
            n += 1
        kth = prev_kth = end_kth = prev_end_kth = None
        dummy = ListNode(next=head)
        node = dummy
        count = 0
        while node:
            if count == k - 1:
                prev_kth = node
                kth = node.next
            if count == n - k:
                prev_end_kth = node
                end_kth = node.next
            node = node.next
            count += 1
        prev_end_kth.next = kth
        prev_kth.next = end_kth
        kth.next,end_kth.next = end_kth.next,kth.next
        return dummy.next