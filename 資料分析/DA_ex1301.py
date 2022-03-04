import statistics

data1 = [1,3,4,5,7,9,2]
x = statistics.mean(data1)
y = statistics.variance(data1)
z = statistics.stdev(data1)

print("mean is:", x)
print("variance :", y)
print("standard deviation of data :", z)