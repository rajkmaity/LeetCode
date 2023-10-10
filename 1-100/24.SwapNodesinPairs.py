# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        first = head
        second= head.next

        while  second :
            first.val,second.val=second.val,first.val
            first=second.next
            if not first:
                return head
            if first.next:
                second = first.next
            else:
                return head
        return head
