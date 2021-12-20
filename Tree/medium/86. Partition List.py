# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_head = ListNode()
        big_head = ListNode()
        small,big = small_head,big_head
        while head:
            if head.val<x:
                small.next = head
                small = head
            else:
                big.next = head
                big = head
            head = head.next
        small.next = big_head.next
        big.next = None
        return small_head.next