# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        
        while(slow):
            slow=slow.next
            try:
                fast=fast.next.next
            except:
                return False
            if slow==fast:
                return True
        else:
            return False
        
        