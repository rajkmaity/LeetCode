# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowpointer=head
        fastpointer=head
        if head == None:
            return False
        while fastpointer != None and fastpointer.next !=None:
            slowpointer= slowpointer.next
            fastpointer=fastpointer.next
            fastpointer=fastpointer.next
            if fastpointer== slowpointer:
                return True
        return False
