from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        firstPointer = headA
        secondPointer = headB

        while firstPointer != secondPointer:
            firstPointer = firstPointer.next if firstPointer != None else headB
            secondPointer = secondPointer.next if secondPointer != None else headA

        return firstPointer
    