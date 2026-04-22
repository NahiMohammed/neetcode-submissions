/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1==null){
            return list2;
        }
        if (list2==null){
            return list1;
        }
        ListNode res=new ListNode();
        int val1 = list1.val;
        int val2 = list2.val;
        if (val1>val2 ){
            res.val=val2;
            res.next=mergeTwoLists(list1,list2.next);

        }else {
            res.val =val1;
            res.next=mergeTwoLists(list1.next,list2);


        }

        return res;
        
    }
}