#coding:utf-8

# Mr. Hu: 这是模块，不涉及到包

class Book:
    lang = 'learn python with laoqi'

    def __init__(self, author):
        self.author = author

    def get_name(self):
        return self.author

def new_book():
    return "数据准备和特征工程"

if __name__ == "__main__":       # Mr. Hu:  调试完之后， import moduel, 得到 __name__ is 'module' NOT '__main__'
    python = Book('laoqi')
    author_name = python.get_name()
    print(author_name)
    published = new_book()
    print(published)