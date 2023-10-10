# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first_point= head
        if head == None:
            return head
        if head.next !=None:
            second_point=head.next
        else :
            return head
        while second_point != None:
            cur_val=first_point.val
            next_val=second_point.val
            if cur_val==next_val:
                first_point.next=second_point.next
                second_point=second_point.next
            else:
                first_point=first_point.next
                second_point=second_point.next
        return head