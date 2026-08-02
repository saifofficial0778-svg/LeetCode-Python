# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        curr=slow
        prev=None

        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        slow=head
        curr=prev
        while curr:
            if slow.val!=curr.val:
                return False
            slow=slow.next
            curr=curr.next
        return True
