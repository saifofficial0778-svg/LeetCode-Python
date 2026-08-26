# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        curr=slow.next
        slow.next=None
        prev=None

        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node

        first=head
        second=prev

        while second:
            p1=first.next
            p2=second.next
            first.next=second
            second.next=p1
            first=p1
            second=p2


        