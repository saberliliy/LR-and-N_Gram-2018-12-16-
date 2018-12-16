import matplotlib.pyplot as plt
import numpy as np
import random


def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    fr.close()
    return dataMat, labelMat



def sigmoid(z):
    g = 1.0 / (1.0 + np.exp(-z))
    return g

def update_weight(Data, Label,time):
    dataMatrix = np.mat(Data)
    labelMat = np.mat(Label).transpose()
    m, n = np.shape(Data)
    alpha = 0.001
    weight = np.ones((n,1))
    for k in range(time):
        h = sigmoid(dataMatrix * weight)
        error = labelMat - h
        weight = weight + alpha * dataMatrix.transpose() * error
    return weight.getA()   #将矩阵转换成数组

def plotBestFit(weights):
    dataMat, labelMat = loadDataSet()
    dataArr = np.array(dataMat)
    n = np.shape(dataMat)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s = 20, c = 'red', marker = 's',alpha=.5)
    ax.scatter(xcord2, ycord2, s = 20, c = 'green',alpha=.5)
    x = np.arange(-3.0, 3.0, 0.1)
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.show()
def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    m,n = np.shape(dataMatrix)
    weights = np.ones(n)
    for j in range(numIter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.01
            randIndex = int(random.uniform(0,len(dataIndex)))
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights

if __name__ == '__main__':
    dataMat, labelMat = loadDataSet()
    weights = update_weight(dataMat, labelMat,300)
    plotBestFit(weights)
