arry = [1,9]
number = ''
list = []
for ele in arry:
    number = number + str(ele)
realnumber = int(number)
realnumber = realnumber + 1
for substring in str(realnumber):
    list.append(substring)
print(list)