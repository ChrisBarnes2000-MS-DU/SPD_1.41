"""Problem: 
    - Given an array nums of integers, return how many of them contain an even number of digits.

    Example Input:
        -Input: nums = [12,345,2,6,7896]

    Example Output:
        -Output: 2

    Explanation: 
    12 contains 2 digits (even number of digits). 
    345 contains 3 digits (odd number of digits). 
    2 contains 1 digit (odd number of digits). 
    6 contains 1 digit (odd number of digits). 
    7896 contains 4 digits (even number of digits). 
    Therefore only 12 and 7896 contain an even number of digits.

-1 Restate the problem
    -
-2 Ask clarifying questions
    -
-3 State your assumptions
    - 1 <= nums.length <= 500
    - 1 <= nums[i] <= 10^5
-4 Think out loud
  -4a Brainstorm solutions
        - split the array into individual numbers
        - split the numbers into individual digits (this is because integers don't have a length)
        - check if the number of digits is even using module %      if so add 1 to count
        - return the count
  -4b Explain your rationale
        -
  -4c Discuss tradeoffs
        -
  -4d Suggest improvements
        -
"""

"""Pseudo Approach
    - [12, 345, 2, 6, 7896]
    index   |   value   |   response    |   T/F     |   Count
      0     |     12    |       0       |   True    |     1
      1     |    345    |       1       |   False   |     1
      2     |     2     |       1       |   False   |     1
      3     |     6     |       1       |   False   |     1
      4     |   7896    |       0       |   True    |     2
    Count = 2

    Edge Cases:
        -

    Complexity Check:
        After implementing some code go back through and revaluate its time and/or space complexity -- refractor/improve/find more edge cases -- repeat
"""

class Solution:
    def findNumbers(self, nums: [int]) -> int:
        count = 0
        for _ in nums:
            if len(list(str(_))) % 2 == 0:
                count += 1
        return count

if __name__ == "__main__":                              # RunTime:
    s = Solution()
    param = [12, 345, 2, 6, 7896]
    function_output = s.findNumbers(param)
    print(function_output)
