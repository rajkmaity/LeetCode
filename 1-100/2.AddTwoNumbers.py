# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result=[]
        residual=0
        if l1==None and l2==None:
            l3=ListNode()
            return l3
        while (l1!=None or l2!=None):
            if l1== None:
                l1_val=0
                l2_val=l2.val
                l2=l2.next
            elif l2==None:
                l1_val=l1.val
                l2_val=0
                l1=l1.next
            else:
                l1_val=l1.val
                l2_val=l2.val
                l1=l1.next
                l2=l2.next
            num3=l1_val + l2_val +residual
            residual= int(num3/10)
            num3= num3 %10
            result.append(num3)
        if residual!=0:
            result.append(residual)
        print(result)

        res=ListNode(result[0],None)
        l3=res
        for item in range (1,len(result)):
            l3.next=ListNode(result[item],None)
            l3=l3.next
        return res