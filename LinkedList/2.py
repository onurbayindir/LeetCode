# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            addition = (l1.val + l2.val) // 10
            curNode = ListNode((l1.val + l2.val) % 10)
            l1 = l1.next
            l2 = l2.next
            head = curNode
            while l1 != None or l2 != None:
                if l1 == None:
                    newNode = ListNode((l2.val + addition) % 10)
                    addition = (addition + l2.val) // 10
                    curNode.next = newNode
                    curNode = curNode.next
                    l2 = l2.next
                elif l2 == None:
                    newNode = ListNode((l1.val + addition) % 10)
                    addition = (addition + l1.val) // 10
                    curNode.next = newNode
                    curNode = curNode.next
                    l1 = l1.next
                else:
                    newNode = ListNode((l1.val+l2.val+addition) % 10)
                    addition = (addition + l1.val+l2.val) // 10
                    curNode.next = newNode
                    curNode = curNode.next
                    l1 = l1.next
                    l2 = l2.next
            if addition:
                curNode.next = ListNode(1)
            return head
                    
                