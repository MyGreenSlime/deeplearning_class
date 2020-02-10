import numpy as np 

Train = [np.array([1,0,0]),np.array([1,1,0]),np.array([1,0,1]),np.array([1,1,1])]
Y = [0,1,1,1]
Weight = np.array([0,0,0])
def perceptron(x,W):
    X = x
    W = W
    ans = np.sum(X*W)
    if(ans > 0):
        return 1
    else :
        return 0

def Cal():
    lr = 1
    global Weight
    checkAll = 0
    while checkAll < 4:
        for index,i in enumerate(Train):
            roundAns = perceptron(i, Weight)
            print(i, Weight, roundAns, Y[index])  # display Input Weight of last layer, PredictValue, Actual Value
            if(roundAns == Y[index]):
                checkAll+=1
            elif(roundAns == 1 and Y[index] == 0):
                Weight = Weight - (lr*i)
                checkAll = 0
            else:
                Weight = Weight + (lr*i)
                checkAll = 0
        

Cal()