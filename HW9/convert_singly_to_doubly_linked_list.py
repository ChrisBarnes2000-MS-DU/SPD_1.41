"""Problem: 
    - convert singly linked list to doubly linked list

    Example Input:
        -1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6

    Example Output:
        -1 <- -> 2 <- -> 6 <- -> 3 <- -> 4 <- -> 5 <- -> 6

-1 Restate the problem
    - convert a linked list from single to double

-2 Ask clarifying questions
    - does the order of imputs matter?

-3 State your assumptions
    - order does matters, there may be duplicates

-4 Think out loud
  -4a Brainstorm solutions
        - loop through each element of the single linked list and keep track of previous current and next pointers
            a. - utilize the loop to iteratively make a new linked list one at a time
            b. - create a list then send it to the init of a double linked list
            c. - add a previous property to the current linked list

  -4b Explain your rationale
        - a. will take the longest, as we have to loop through each element then append/add it to a new linked list
        - b. this is probably the best way to do it as you gust do a pull for the values as a list then send it to a doubly linked list init
            -- similar to a but only runs relatively once..
        - c. this is doable in python but not all languages.. also messes up the overall structure of the instance's linked-list

  -4c Discuss tradeoffs
        - c. doesn't deal with creating/using up any more memory space while b. would be the most efficient and similar to a.

  -4d Suggest improvements
        -
"""

"""Pseudo Approach
    - Pull the list of values from the linked list, pass them to the init of the doubly linked list and return it..

    Edge Cases:
        -

    Complexity Check:
        After implementing some code go back through and revaluate its time and/or space complexity -- refractor/improve/find more edge cases -- repeat
"""

import sys

sys.path.append('/Users/ChrisBarnes/dev/CS/CS-1.2-Intro-Data-Structures/Code')

from doubleylinkedlist import DoublyLinkedList
from linkedlist import LinkedList

if __name__ == "__main__":                              # RunTime:
    sl = LinkedList([1, 2, 6, 3, 4, 5, 6])
    values = sl.items()
    print(sl)
    dl = DoublyLinkedList(values)
    print(dl)