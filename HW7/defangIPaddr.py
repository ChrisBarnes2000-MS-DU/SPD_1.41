"""Problem: 
    -

    Example Input:
        -

    Example Output:
        -

-1 Restate the problem
    -
-2 Ask clarifying questions
    -
-3 State your assumptions
    -
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
    -

    Edge Cases:
        -

    Complexity Check:
        After implementing some code go back through and revaluate its time and/or space complexity -- refractor/improve/find more edge cases -- repeat
"""

from re import sub

class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = sub("\.", "[.]", address)
        return address

if __name__ == "__main__":                              # RunTime:
    s = Solution()
    param = "1.1.1.1"
    function_output = s.defangIPaddr(param)
    print(param)
    print(function_output)
