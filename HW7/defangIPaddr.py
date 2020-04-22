"""Problem: 
    - Given a valid (IPv4) IP address, return a defanged version of that IP address.
      A defanged IP address replaces every period "." with "[.]".

    Example Input:
        - Input: address = "1.1.1.1"
        - Input: address = "255.100.50.0"

    Example Output:
        - Output: "1[.]1[.]1[.]1"
        - Output: "255[.]100[.]50[.]0"

-1 Restate the problem
    - add brackets around the period in an ipv4 address i.e defang it
-2 Ask clarifying questions
    - Can we use regex?

-3 State your assumptions
    - The given address is a valid IPv4 address.

-4 Think out loud
  -4a Brainstorm solutions
        - use regex to substitue/replace any \. with [.]
  -4b Explain your rationale
        - regex makes it simple and more powerful
        - (we need to use \ to escape the . or it would just do it for any/all characters)
  -4c Discuss tradeoffs
        -
  -4d Suggest improvements
        -
"""

"""Pseudo Approach
    - split the ip/string into characters, loop through them looking for a . and add [] to it then rejoing the string/ip and return it

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
