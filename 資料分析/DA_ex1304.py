import numpy as np
import stats as sts
scares = [31,24,23,25,14,25,13,12,14,23,
          32,34,43,41,21,23,26,26,34,42,
          43,25,24,23,24,44,23,14,52,32,
          42,44,35,28,17,21,32,42,12,34]

print('求和：', np.sum(scares))
print('個數：', len(scares))
print('平均值：', np.mean(scares))
print('中位數：', np.median(scares))
print('眾數：', sts.mode(scares))
print('上四分位數：', sts.quantile(scares,p=0.25))
print('下四分位數：', sts.quantile(scares,p=0.75))

print('最大值：', np.max(scares))
print('最小值：', np.min(scares))
print('極差：', np.std(scares))
print('四分位數：', sts.quantile(scares,p=0.75), sts.quantile(scares,p=0.25))
print('標準差：', np.std(scares))
print('方差', np.var(scares))
print('離散係數', np.std(scares)/np.mean(scares))

print('遍度：', sts.skewness(scares))
print('峰度：', sts.kurtosis(scares))

