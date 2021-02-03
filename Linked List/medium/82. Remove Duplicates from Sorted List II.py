# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Time: O(n)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
            
        while head:
            if head.next and head.val==head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
                head = head.next
                continue
            prev = head
            head = head.next
        return dummy.next