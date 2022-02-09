# coding: utf-8
'''
input the digits ==> display their english 
For example:
  "250" == > "two five zero"
'''

digits = list(range(10))
for k, v in enumerate(digits):
    digits[k] = str(v)

english = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

mydict = {}
for d, e in zip(digits, english):
    mydict[d] = e

print(mydict)

number = input("Please input a integer: ")
rst = []
for c in list(number):
    rst.append(mydict[c])

result = " ".join(rst)
print(f"{number} ===> {result}")

