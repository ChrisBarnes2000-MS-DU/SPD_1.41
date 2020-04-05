"""Problem: Given an array a of n numbers and a target value t,
            find two numbers in a that sum to t.

    Example input:
        a=[5, 3, 6, 8, 2, 4, 7] and t=10
        ⇒  output: [3, 7] or [6, 4] or [8, 2]
"""

"""Pseudo Approach
    look at each item subtract it from the list, save as remainder variable
    look through the list for remainder if found
        add the index of the number and remainder to one list and
        add the number and remainder to a second list
    after viewing all possible options return/print the 2 lists

    Edge Cases:
        loop range issues
        number and remainder have
            same indexes
            reverse indexes

    Complexity Check:
        After implementing some code go back through and revaluate its time and/or space complexity -- refractor/improve/find more edge cases -- repeat
"""

if __name__ == "__main__":                              # RunTime:
    a = [5, 3, 6, 8, 2, 4, 7]                                   # O(1) To declare a list of values
    print("Current List: \t", a)                                # O(1) To print
    t = int(input("Target Value: \t "))                         # O(?) Not sure the time complexity of input (1)
    output_inds = []        #  ---                              # O(1) To declare variables or lists
    outputs = []            # /

    for num_ind in range(len(a)):                               # O(n) n being length of list a
        remainder = t - a[num_ind]                              # O(1) Constant time to assert variable checks
        print(
            "\nlist: \t", a,
            "\ntarget: ", t,
            "\ncurrent: \t", a[num_ind],
            "\nremainder: \t", remainder,
            )
        # Found Edge Case: Solution add -1 to range()
        for remainder_ind in range(len(a) -1):                  # O(n) n-1 being length of list a
            possible = a[remainder_ind] == remainder            # O(1) Constant time to asset variable checks
            # Found Edge Case: Solution add an if check statement for same_index
            same_ind = num_ind == remainder_ind                 # O(1) Constant time to assert variable checks
            # Found Edge Case: Solution add a check statement for if remainder index is pass number index already
            used_ind = remainder_ind > num_ind                  # O(1) Constant time to asset variable checks
            if possible and not same_ind and not used_ind:      # O(1) For boolean if statements
                print("Possible: At index: {}, {} matches the remainder"
                      .format(remainder_ind, remainder))        # O(1) To print
                output_inds.append((num_ind, remainder_ind))    # O(1) To append to a list
                outputs.append((a[num_ind], a[remainder_ind]))  # O(1) To append to a list

        if num_ind == len(a)-1:
            print("----Final----")
        else:
            print("----next----")

    print("Output:  {} \nIndexes: {}".format(outputs, output_inds)) 
