# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag = False
        ans = l1
        while True:
            temp = l1.val + l2.val
            if flag:
                temp += 1
            if temp >= 10:
                flag = True
                l1.val = temp-10
            else:
                flag = False
                l1.val = temp
            if l1.next and not l2.next:
                l2.next = ListNode()
            elif not l1.next and l2.next:
                l1.next = ListNode()
            elif not l1.next and not l2.next and flag:
                l1.next = ListNode()
                l2.next = ListNode()
            elif not l1.next and not l2.next and not flag:
                break
            l1 = l1.next
            l2 = l2.next


        return ans
                
            
