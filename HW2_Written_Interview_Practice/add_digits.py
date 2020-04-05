"""
Problem:
    Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
    Input: 38
    Output: 2 
    Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
                Since 2 has only one digit, return it.

Follow up:
    Could you do it without any loop/recursion in O(1) runtime?


-1 Restate the problem
    given a big number above 0 add all its digits until there is only 1
-2 Ask clarifying questions
    -
-3 State your assumptions
    -
-4 Think out loud
  -4a Brainstorm solutions
        (while) loop, take in a number separate it and add them together then pass it back & repeat
        
        recursion take in a number separate it and add them together then pass it back & repeat
        
  -4b Explain your rationale
        Don't like recursion very much but may be easier as we are just repating the same 2 things and will need to pass values through to its self, where as a loop is less friendly to using params, value systems..
        
  -4c Discuss tradeoffs
        -
  -4d Suggest improvements
        -
"""


class Solution:
    def addDigits(self, num: int) -> int:
        digits = [int(i) for i in str(num)]
        print(num, " --> ", digits)
        size = len(digits)
        print("size", size, "output", num, "\n")
        if size == 1: return num
        else:
            out = 0
            for digit in digits:
                out += digit
            out + self.addDigits(out)
            # return out



if __name__ == "__main__":
    my_solution = Solution()
    result = my_solution.addDigits(38)
    print(result, "\n")
    # result = my_solution.addDigits(45)
    # print(result, "\n")
    # result = my_solution.addDigits(673)
    # print(result, "\n")
    # result = my_solution.addDigits(9034)
    # print(result, "\n")
    # result = my_solution.addDigits(24537)
    # print(result, "\n")
