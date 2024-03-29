# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        
        while(fast):
            if slow.next==None:
                return slow
            slow=slow.next
            
            try:
                fast=fast.next.next
            except:
                return slow
            
            try:
                if fast.next==None:
                    return slow
            except:
                return slow
        