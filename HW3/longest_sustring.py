# Find the longest substring of unique letters in a given string of n letters.
# antidisestablishmentarianism  --> antid, dise, establi, tablishmentar

"""antidisestablishmentarianism
antidi          broken by i
dises           broken by s
establis        broken by s
tablishmentari  broken by i
shmentariani    broken by i
sm              broken by end of line
The longest substring is:    tablishmentari """

"""Simpler example
we'll use -x- as our re occuring letter to break from
input xabcdxabcdefghxklmnxjk
broken up we find that
xabcd
xabcdefgh
xklmn
xjk
the longest substring is:    xabcdefgh """


def longest_substring(letters):
    substrings = substring(letters)
    longest_substring = largest(substrings)
    return longest_substring

def substring(letters):
    substring = ''
    possible = []
    letters = list(letters)
    for letter in letters:
        if letter not in substring:
            substring += letter
        else:
        # if substring not in possible:
            possible.append(substring)
            # substring = ''
    print(possible)
    return possible

def largest(substrings):
    largest = max(substrings)
    print(largest)
    return largest


if __name__ == "__main__":
    letters = 'xabcdxabcdefghxklmnxjk'
    print(longest_substring(letters))
    # longest_substring(letters)
