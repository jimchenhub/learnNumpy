# -*- coding: utf-8 -*-
import numpy as np

# average求加权平均值
c = [20,30,40,50,60]
v = [5,6,7,3,5]
vwap = np.average(c, weights=v)
print "VWAP = ", vwap

# 算数平均值
print "mean = ", np.mean(c)

# 时间加权平均（最近的价格更重要）
t = np.arange(len(c))
twap = np.average(c, weights=t)
print "TWAP = ", twap