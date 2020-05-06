"""Problem: 
    - Remove all elements from a linked list of integers that have value val.

    Example Input:
        -1->2->6->3->4->5->6, val = 6

    Example Output:
        -1->2->3->4->5
"""

"""Interview Steps
-1 Restate the problem
    - Remove all elements from a linked list of integers that have value val.
-2 Ask clarifying questions
    - Will it be a double or singly linked list?
    - How many duplicates/occurrences of the target can we expext?
    - do we care about modifying the original linked list
-3 State your assumptions
    - Only worry about a singly linked list
    - There may be any amount of occurrences
-4 Think out loud
  -4a Brainstorm solutions
        - Somehow loop thorugh each element keeping track of prev current and next and compare currents value and reroute if we find a match
  -4b Explain your rationale
        - We could either be done recursively or iteratively, I dislike recursion so I went with a while loop either which way the complexity would be O(n)
  -4c Discuss tradeoffs
        - 
  -4d Suggest improvements
        -
"""

"""Pseudo Approach
    - Check if the current element is what value we want to remove,
        if not at the end and not what we want to remove go the the next one,
        check again, if/when we find a match update pervious' next pointer to
        current's next pointer, effectively removing the current item, then
        proceed till we get to the end.

    Edge Cases:
        - There was no occurrence of our target value, then nothing is to be changed

    Complexity Check:
        After implementing some code go back through and revaluate its time and/or space complexity -- refractor/improve/find more edge cases -- repeat
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return

        prev, curr = head, head
        while curr is not None:
            if head.val == val:
                head = curr.next
                prev = curr = head

            elif curr.val == val:
                prev.next = curr.next
                curr = prev.next

            else:
                prev = curr
                curr = curr.next

        return head
