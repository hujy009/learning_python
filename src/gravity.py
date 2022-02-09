#coding:utf-8
'''
G = mg, g=9.8
'''

def w(m, g):
    return m * g

def weight(g):
    def cal_mg(m):
        return m * g
    return cal_mg

w = weight(10)    # g = 10
G = w(100)
G2 = w(50)
print(G)

w2 = weight(9.78046)
G3 = w2(100)
print(G3)