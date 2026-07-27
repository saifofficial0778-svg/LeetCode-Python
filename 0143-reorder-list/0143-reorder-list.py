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

        curr = slow.next
        slow.next = None
        prev=None

        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node

        first=head
        second=prev
        
        while second:
            tmp1=first.next
            tmp2=second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2
            
