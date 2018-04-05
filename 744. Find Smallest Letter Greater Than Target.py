# Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.
#
# Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.
#
# Examples:
# Input:
# letters = ["c", "f", "j"]
# target = "a"
# Output: "c"
#
# Input:
# letters = ["c", "f", "j"]
# target = "c"
# Output: "f"
#
# Input:
# letters = ["c", "f", "j"]
# target = "d"
# Output: "f"
#
# Input:
# letters = ["c", "f", "j"]
# target = "g"
# Output: "j"
#
# Input:
# letters = ["c", "f", "j"]
# target = "j"
# Output: "c"
#
# Input:
# letters = ["c", "f", "j"]
# target = "k"
# Output: "c"
# Note:
# 1.letters has a length in range [2, 10000].
# 2.letters consists of lowercase letters, and contains at least 2 unique letters.
# 3.target is a lowercase letter.
import string

letters = ["c", "f", "j"]
target = "k"

dic ={}
list = []
list2 = []
number = 0
for letter in string.ascii_lowercase:
        dic[letter] = number + 1
        number = number + 1
for element in letters:
    if dic[element] > dic[target]:
        list.append(dic[element] - dic[target])
    else:
        list2.append(dic[element])
if list != []:
    minnum = min(list)
    print(string.ascii_lowercase[dic[target]+minnum-1])
else:
    minnum =min(list2)
    print(string.ascii_lowercase[minnum-1])








