# coding: utf-8

"""
Create a data set including 1 to 10 randomly, the nubmer is 100;
calculate the frequence of each number
"""

import numpy as np
import numpy.random as npr

ary = npr.randint(1, 11, size=100)
cnt = {}
for v in ary:
    if v in cnt:
        cnt[v] += 1
    else:
        cnt[v] = 1

# for k, v in cnt.items():
#     print(f"{k} : {v}")
print(cnt)