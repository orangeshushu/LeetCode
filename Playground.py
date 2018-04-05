from collections import defaultdict
strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')


print(defaultdict.__missing__.__doc__)


# for i in strings:counts.setdefault(i, 0)
#     if i not in counts:
#         counts[i] = 1
#     else:
#         counts[i] += 1
# print(counts)

# for i in strings:
#     counts[i] = counts.setdefault(i, 0) + 1
# print(counts)
# print(counts.setdefault('kitten', 0))

