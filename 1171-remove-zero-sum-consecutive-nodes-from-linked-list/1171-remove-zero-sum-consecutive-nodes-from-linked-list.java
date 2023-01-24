class Solution {
    public ListNode removeZeroSumSublists(ListNode head) {

        ListNode dummy = new ListNode(0) ;
        dummy.next = head ;
        ListNode temp1 ;
        ListNode temp2 ;

        for(temp1 = dummy ; temp1!=null ; temp1 = temp1.next)
        {
            int sum  = 0;
            for(temp2 = temp1.next ; temp2!=null ; temp2 = temp2.next)
            {
                sum += temp2.val ;
                if(sum == 0)
                    temp1.next = temp2.next ;
            }
        }
        return dummy.next ;
    }
}