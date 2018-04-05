# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".


a = "11"
b = "1"
deca = int(a, 2)
decb = int(b, 2)
decsum = deca + decb
print(bin(decsum)[2:])
