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
        first_half=head
        second_half=prev
        while second_half:
            p1=first_half.next
            p2=second_half.next
            first_half.next=second_half
            second_half.next=p1
            first_half=p1
            second_half=p2
            