# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.
import string
transfrom = ''
str = "A man, a plan, a ccanal: Panama"
str = str.lower()
for element in str:
    print(element)
    if (element in string.ascii_lowercase) or (element in string.digits):
                transfrom = transfrom + element
print(transfrom, end='')
length = len(transfrom)
print(length)
if length % 2 == 0:
    print(length/2)
    for substring in range(int(length/2)):
        print(substring)
        if transfrom[(substring+1)] != transfrom[-(substring+1)]:
              print('Flase')
    print('True')
if length % 2 != 0:
    for sstring in range(int(length/2)):
        if transfrom[(sstring+1)] != transfrom[-(sstring+1)]:
            print('False')
    print('True')