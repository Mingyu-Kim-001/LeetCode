# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(n), Extra space: O(1)
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k==1: return head
        length = 0
        iterhead = head
        while iterhead:
            length+=1
            iterhead = iterhead.next
        
        init = ListNode(val=-1)
        init.next = head
        veryPrev = init
        for _ in range(length//k):
            prev = veryPrev
            for __ in range(k):
                # print(veryPrev.val,prev.val,head.val)
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            veryPrev.next.next = head
            temp = prev
            prev = veryPrev.next
            veryPrev.next = temp
            veryPrev = prev
        return init.next