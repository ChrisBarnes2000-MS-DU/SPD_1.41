"""Problem: 
    Given an array a of n numbers and a count k find the k largest values in the array a.

    Example Input:
        a=[5, 1, 3, 6, 8, 2, 4, 7] and k=3

    Example Output:
        [6, 8, 7]

"""

"""Pseudo Approach
    loop through array keeping track of a current value form the array and a max value seen
        - start just for 1st largest so we can use max() later we pass to array k_lagest


    and keep track of the largest k number of vales

    Edge Cases:
        -

    Complexity Check:
        After implementing some code go back through and revaluate its time and/or space complexity -- refractor/improve/find more edge cases -- repeat
"""

def find_absolute_largest(array):
    return max(array)

def find_k_largest(array, k):   # overall Runtime: being k <= n,
                                # O(n+k*(n+n)) -> O(n+2nk) -> O(n+nk), -> O(nk)
    outputs = []                    # O(1)
    array = list(array)             # O(n) n being length/size of array
    for _ in range(k):              # O(k) number of largest numbers
        largest = max(array)        # O(n) m being size of new array
        outputs.append(largest)     # O(1)* to append to the end
        array.remove(largest)       # O(n)
    return outputs                  # O(1)

if __name__ == "__main__":                              # RunTime:
    a = [5, 1, 3, 6, 8, 2, 4, 7]
    # k = int(intput("number of largesst values: "))
    k = 3
    k_largest = find_k_largest(a, k)
    print(a)
    print(k_largest)
