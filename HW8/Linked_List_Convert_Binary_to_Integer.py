"""Problem: 
    - Convert Binary Number in a Linked List to Integer
    Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

    Return the decimal value of the number in the linked list.

    Example Input:
        - 1 --> 0 --> 1

    Example Output:
        - 5

-1 Restate the problem
    - Pull out the binary number as linkedlist and convert it to an integer

-2 Ask clarifying questions
    - 

-3 State your assumptions
    - The Linked List is not empty.
    - Number of nodes will not exceed 30.
    - Each node's value is either 0 or 1.

-4 Think out loud
  -4a Brainstorm solutions
        -

  -4b Explain your rationale
        -

  -4c Discuss tradeoffs
        -

  -4d Suggest improvements
        -

"""

"""Pseudo Approach
    - loop through nodes of linked list pull out value and add to string convert binary string to int

    Edge Cases:
        -

    Complexity Check:
        After implementing some code go back through and revaluate its time and/or space complexity -- refractor/improve/find more edge cases -- repeat
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:           #Over-all O(n)
        value = ""                                          # O(1)
        while head is not None:                             # O(n)
            value += str(head.val)                          # O(1)
            head = head.next                                # O(1)
        return int(value, 2)                                # O(1)


if __name__ == "__main__":                              # RunTime: Over-all O(n)
    s = Solution()
    input_head = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    function_output = s.getDecimalValue(input_head)
    print(function_output, "Output should be: 18880")
