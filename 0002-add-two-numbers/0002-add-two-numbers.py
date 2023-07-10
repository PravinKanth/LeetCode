# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        s2=""
        temp1=l1
        while temp1:
            s1+=str(temp1.val)
            temp1=temp1.next
        temp2=l2
        while temp2:
            s2+=str(temp2.val)
            temp2=temp2.next
        s1=s1[::-1]
        s2=s2[::-1]
        sum1=str(int(s1)+int(s2))[::-1]
        ll=ListNode()
        temp=ll
        for i in range(len(sum1)):
            ll.val=sum1[i]
            if i==len(sum1)-1:
                ll.next=None
            else:    
                ll.next=ListNode()
                ll=ll.next
        return temp      
            
            
        
        