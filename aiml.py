import matplotlib.pyplot as pl
import random
def plot(slopeee, intercepttt):
    pl.xlim(0,10)
    pl.ylim(0,10)
    for pt in range(0, len(xSet)):
        pl.plot(xSet[pt], ySet[pt], marker="o", color="red")
    pl.plot(xSetMean, ySetMean, marker="o", markersize = 10, color="blue")
    pl.axline((0,intercepttt), slope = slopeee)
    #pl.legend("Slope:"+  str(slopeee))
    pl.show()

def calculateRSS(slope, intercept):
    errors = []
    rss = 0
    for i in range(0,len(xSet)):
        predictedY = ySet[i]
        actualY = slope * xSet[i]
        actualY = actualY + intercept
        error = predictedY - actualY
        errors.append(error)
        rss = rss + error**2
    return rss

xSet = [4,2,9,4,7,3,8,2,4,3]
ySet = [4,5,6,6,2,7,3,4,7,9]

xSetMean = 0
for x in xSet:
    xSetMean = xSetMean + x
xSetMean = round(xSetMean / len(xSet),5)


ySetMean = 0
for y in ySet:
    ySetMean = ySetMean + y
ySetMean = ySetMean / len(ySet)


#A = X - XMean
#B = Y - YMean
A, B = [], []
for i in range(0,len(xSet)):
    A.append(round(xSet[i] - xSetMean, 5))
    B.append(round(ySet[i] - ySetMean, 5))


#C = X - XMean squared
C, D = [], []
for i in range(0,len(A)):
    C.append(A[i] ** 2)
    D.append(A[i] * B[i])

slope = sum(D)/sum(C)
intercept = ySetMean - slope*xSetMean

print("xSet\t:", xSet)
print("ySet\t:", ySet)
print("XMean\t:", xSetMean)
print("YMean\t:", ySetMean)
print('A\t:', A)
print('B\t:', B)
print("C\t:", C, sum(C))
print("D\t:", D, sum(D))
print("Slope\t:", slope)
print("Icept\t:", intercept)
#print("Errors\t:",errors)
print("RSS\t:",calculateRSS(slope, intercept))
plot(slope, intercept)


#begins
e1 = calculateRSS(slope, intercept)
#for i in range(0,10000):
#    e2 = calculateRSS(random.randrange(1000)/1000, intercept)
#    if e2 < e1: print(e2)

uSLim, lSLim = 1,-1
uILim, lILim = 10, -10
for i in range(0,10):
    randSlope = random.randrange(lSLim * 1000,uSLim * 1000)/1000
    randIntercept = random.randrange(lILim * 1000, uILim * 1000)/1000
    e2 = calculateRSS(randSlope, randIntercept)
    if e2 > e1:
        if randSlope > slope:
            uSLim = randSlope
        if randSlope < slope:
            lSLim = randSlope
        if randIntercept > intercept:
            uILim = randIntercept
        if randIntercept < intercept:
            lILim = randIntercept
    print("RANDOM RSS:", e2)
    plot(randSlope, randIntercept)