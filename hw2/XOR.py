import numpy as np 

Train = [np.array([1,0,0]),np.array([1,1,0]),np.array([1,0,1]),np.array([1,1,1])]
Y = [0,1,1,0]
Weight1 = np.array([-2,1,2]) #for AND Gate
Weight2 = np.array([0,1,1]) #for OR Gate
Weight3 = np.array([0,0,0]) #for Calulate weight of layer 2

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
    global Weight3
    checkAll = 0
    while checkAll < 4:
        for index,i in enumerate(Train):
            AND = perceptron(i, Weight1)
            OR = perceptron(i, Weight2)
            output_layer1 = np.array([1,AND,OR])
            roundAns = perceptron(output_layer1, Weight3)
            print(i, Weight3, roundAns, Y[index]) # display Input Weight of last layer, PredictValue, Actual Value
            if(roundAns == Y[index]):
                checkAll+=1
            elif(roundAns == 1 and Y[index] == 0):
                Weight3 = Weight3 - (lr*output_layer1)
                checkAll = 0
            else:
                Weight3 = Weight3 .+ (lr*output_layer1)
                checkAll = 0
Cal()        