# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer = head
        linked = set()
        while pointer and pointer.next:
            if pointer.next in linked:
                return True
            linked.add(pointer.next)
            pointer = pointer.next
        return False
