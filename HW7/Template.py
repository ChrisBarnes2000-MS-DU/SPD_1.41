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


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for _ in nums:
            if len(list(str(_))) % 2 == 0:
                count += 1
        return count

if __name__ == "__main__":                              # RunTime:
    findNumbers = Solution.findNumbers()
    param = [12, 345, 2, 6, 7896]
    function_output = findNumbers(param)
    print(function_output)
