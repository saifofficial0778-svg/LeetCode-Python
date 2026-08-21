# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):

        if head is None or head.next is None or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        before = dummy

        for _ in range(left - 1):
            before = before.next

        curr = before.next
        prev = None

        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        before.next.next = curr
        before.next = prev

        return dummy.next