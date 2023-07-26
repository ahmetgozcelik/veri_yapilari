from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leftPointer = head
        rightPointer = head

        while n > 0 and rightPointer:
            rightPointer = rightPointer.next
            n -= 1

        while rightPointer and rightPointer.next:
            leftPointer = leftPointer.next
            rightPointer = rightPointer.next

        if leftPointer == head and not rightPointer:
            return head.next

        leftPointer.next = leftPointer.next.next

        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


solution = Solution()
new_head = solution.removeNthFromEnd(head, 2)


while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
