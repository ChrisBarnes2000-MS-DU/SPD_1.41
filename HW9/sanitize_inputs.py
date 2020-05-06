"""Problem: 
    - write a function to sanitize the user inputs

    Example Input:
        -

    Example Output:
        -

-1 Restate the problem
    - sanitize user inputs

-2 Ask clarifying questions
    - Do we need to worry about none alpha characters like numbers and/or punctuation
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
    #gets user input and returns a response
    def prompt_usr(self, prompt, typ):
        if typ == "number":
            response = input(prompt)
            while not response.isnumeric():
                print("Try again: ")
                response = input(prompt)
            #print("Entering response {}".format(response))
            return int(response)
        elif typ == "string":
            response = input(prompt)
            while not response.isalpha():
                print("try again: ")
                response = input(prompt)
            #print("Entering response {}".format(response))
            return str(response)


if __name__ == "__main__":                              # RunTime:
    s = Solution()
    param = None
    function_output = s.function_name(param)
    print(function_output)
