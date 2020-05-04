"""Problem: 
    - Create Target Array in the Given Order
    Given two arrays of integers nums and index. Your task is to create target array under the following rules:

    Initially target array is empty.
    From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
    Repeat the previous step until there are no elements to read in nums and index.
    Return the target array.

    It is guaranteed that the insertion operations will be valid.

    Example Input:
        - Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]        or      nums = [1,2,3,4,0], index = [0,1,2,3,0]

    Explanation:
        nums       index     target                             |       nums       index     target
        0            0        [0]                               |       1            0        [1]
        1            1        [0,1]                             |       2            1        [1,2]
        2            2        [0,1,2]                           |       3            2        [1,2,3]
        3            2        [0,1,3,2]                         |       4            3        [1,2,3,4]
        4            1        [0,4,1,3,2]                       |       0            0        [0,1,2,3,4]

    Example Output:
        - Output: [0,4,1,3,2]                                   or      [0,1,2,3,4]

-1 Restate the problem
    - Rearane the given list into the new index list

-2 Ask clarifying questions
    -

-3 State your assumptions
    - 1 <= nums.length, index.length <= 100
    - nums.length == index.length
    - 0 <= nums[i] <= 100
    - 0 <= index[i] <= i

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
    - loop through the list and adjust them to the new index position

    Edge Cases:
        -

    Complexity Check:
        After implementing some code go back through and revaluate its time and/or space complexity -- refractor/improve/find more edge cases -- repeat
"""

class Solution:                                                             # RunTime:
    def createTargetArray(self, nums: [int], index: [int]) -> [int]:
        output = []                                                         # O(1)
        for i, num in enumerate(nums):                                      # O(n) based on nums size
            output.insert(index[i], num)                                    # O(n) needs to adjust all values to the right of index being inserted at
        return output                                                       # O(1)

if __name__ == "__main__":                              # RunTime:          O(n^2) or O(n)
    nums, indexes = [1, 2, 3, 4, 0], [0,1,2,3,0]
    s = Solution()
    function_output = s.createTargetArray(nums, indexes)
    print(function_output)
