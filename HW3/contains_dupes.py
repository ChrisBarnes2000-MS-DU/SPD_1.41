# Problem: Given a list of n numbers, determine if it contains any duplicate numbers. Example:	nums = [5, 6, 7, 8, 8, 9, 13]	→ 	True: 8 is duped
# https://docs.google.com/document/d/1KAxAKUNNt2wjVd5Ely4465EkJ6yc3bG2IZykRpx-Abc/edit?usp=sharing


def find_dups(arry):
    # Either O(n) or O(n ^ 2) runtime complexity
    # Space complexity O(1)

    # Time complexity O(n)
    # Space complexity O(n)
    for i in range(len(arry)):
        for j in range(len(arry)):
            if arry[i] == arry[j] and i is not j:
                return True

def histo_dups(arry):
    # Runtime: O(n+n)
    hist = {}
    for item in arry:
        hist[item] = hist.get[item, 0] + 1
        if item in hist.values() > 1:
            return True


if __name__ == "__main__":
    nums = [5, 6, 7, 8, 8, 9, 13]

    print(find_dups(nums))
    print(histo_dups(nums))
