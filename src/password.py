#coding:utf-8
'''
编写程序，利用“凯撒密码”方案，实现对用户输入文字的加密操作。

凯撒密码（英語：Caesar cipher），是一种最简单且最广为人知的加密技术。它是一种替换加密的技术，明文中的所有字母都在字母表上向后（或向前）按照一个固定数目进行偏移後被替换成密文。例如，当偏移量是3的时候，所有的字母A将被替换成D，B变成E，以此类推。
'''

letter = input("Please input an English letter: ")
n = 3
pwd = ord(letter) + n
pwd_letter = chr(pwd)
print(letter, "==>", pwd_letter)
