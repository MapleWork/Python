import numpy as np
import statistics

y = [1,3,4,5,8,9,2]

total = sum((y-np.mean(y))**2)

print(y)
print("平均數：", statistics.mean(y))
print("離散平方和：", total)