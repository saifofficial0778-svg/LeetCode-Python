# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next :
            return head

        dummy=ListNode(0)
        dummy.next=head

        prev=dummy

        while prev.next and prev.next.next:
            first=prev.next
            second=first.next

            first.next=second.next
            prev.next=second
            second.next=first
            prev=first

        return dummy.next
            