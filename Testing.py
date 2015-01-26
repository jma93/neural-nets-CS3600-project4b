from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt

def average(list):
    return sum(list)/float(len(list))

def stDeviation(list):
    mean = average(list)
    diffSq = [pow((val-mean),2) for val in list]
    return sqrt(sum(diffSq)/len(list))

penData = buildExamplesFromPenData() 
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)

    
def stddev(values):
    mean = sum(values)/float(len(values))
    differencetotal = 0
    for value in values:
        differencetotal += abs(value - mean)**2
    differencetotal /= float(len(values))
    return sqrt(differencetotal)

    
"""
pen = []
car = []
for x in range(5):
    print "Pen test number:", x+1
    result = testPenData()
    pen.append(result[1])
    print "Car test number:", x+1
    result = testCarData()
    car.append(result[1])
f = open("testingresults.txt", "w")
f.write( "Pen Data Avg, Max, Stdev: " + str((sum(pen)/float(len(pen)))) + ", " + str(max(pen)) + ", " + str(stddev(pen)) + "\n"  )
f.write( "Car Data Avg, Max, Stdev: " + str((sum(car)/float(len(car)))) + ", " + str(max(car)) + ", " + str(stddev(car)) + "\n"  )

f.write("\n\n\n")

for y in range(0,41,5):
    pen = []
    car = []
    for x in range(5):
        print "Pen test number:", x+1, "y:", y
        result = testPenData([y])
        pen.append(result[1])
        print "Car test number:", x+1, "y:", y
        result = testCarData([y])
        car.append(result[1])
    f.write( "Pen Data Avg, Max, Stdev: " + str((sum(pen)/float(len(pen)))) + ", " + str(max(pen)) + ", " + str(stddev(pen)) + "\n" )
    f.write( "Car Data Avg, Max, Stdev: " + str((sum(car)/float(len(car)))) + ", " + str(max(car)) + ", " + str(stddev(car)) + "\n" )
f.close()
"""
#car = testCarData([5])
car = []
for x in range(5):
    print "Car test number:", x+1
    result = testCarData([0])
    car.append(result[1])
print "Car Data Avg, Max, Stdev: " + str((sum(car)/float(len(car)))) + ", " + str(max(car)) + ", " + str(stddev(car))

