import random

def dice():
    return random.randint(1,6)

def ex():
    X = dice()
    Y = dice()
    return X+Y == 7

def simulate(experiment, times):
    success = 0
    for i in range(times):
        if experiment():
            success+=1
    return success/times

print(simulate(ex, 100))
print(simulate(ex, 1000))
print(simulate(ex, 10000))
print(simulate(ex, 100000))
