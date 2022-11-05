import pandas as pd
from matplotlib import pyplot as plt
import math
import os
import csv
# os.system('cls')
df = pd.read_csv('100+3.csv')

df = df.reset_index()


def euclidean_distance(x1: int, y1: int, x2: int, y2: int):
    return math.dist([x1, y1], [x2, y2])


def checkArr(shrList, id):
    for i in shrList:
        if id == i[0]:
            return True
    return False


def return_csv():
    f = open('./result.csv', 'w')
    writer = csv.writer(f)
    for i in shrList:
        writer.writerow(i)
    

def checkDups(shrList):
    seen = set()
    for item in shrList:
        t = tuple(item)
        if t not in seen:
            seen.add(t)
        else:
            return True
    return False


arr = []
dist = {}
dist2 = {}
for index, row in df.iterrows():
    if row['type'] != "resupply":
        dist[row['index']] = [row['x'], row['y'],
            row['type'], row['patient_count']]
    else:
        dist2[row['index']] = [row['x'], row['y'],
            row['type'], row['patient_count']]


startNode = 0
nextNode = float('inf')
supplyNode = float('inf')
shrList = []
shrList.append([startNode, 0])
val = 0
maxUnits = 1000
patient_count = 0
count = 0
while checkDups(shrList) == False and maxUnits > 0:
    if startNode in dist:
        arr = dist[startNode]
    else:
        arr = dist2[startNode]
    shorDistance = float('inf')
    # Select shortest distance to next node non-resupply
    for j in dist.keys():
        if j != startNode and not checkArr(shrList, j):
            val = euclidean_distance(arr[0], arr[1], dist[j][0], dist[j][1])
            if val < shorDistance:
                shorDistance = val
                nextNode = j

    # Check closet resupply station
    shorDistance2 = float('inf')
    for k in dist2.keys():
        val = euclidean_distance(
            dist[nextNode][0], dist[nextNode][1], dist2[k][0], dist2[k][1])
        if val < shorDistance2:
            shorDistance2 = val
            supplyNode = k

    if math.isinf(shorDistance) == False and math.isinf(shorDistance2) == False:

        # Check if the distance from current node to next is greater than next node distance + resupply distance
        if(count == 5 ):
            # Go to resupply station
            count = 0
            startNode = supplyNode
            maxUnits = 1000
            print(f'Going to resupply!')
        elif maxUnits - shorDistance > 0:
            maxUnits -= shorDistance
            count +=1
            if startNode in dist:
                patient_count += dist[startNode][3]

            shrList.append([nextNode, shorDistance])
            startNode = nextNode
            print(
                f"Distance: {shorDistance} MaxUnits: {maxUnits} Patient count: {patient_count}")
        else:
            return_csv()
            print(f'DONE Patient count: {patient_count}')
            break

# print("Starting node: " + str(0))
# for j in shrList:
#     print("Next Node: " + str(j[0]) + " Distance: " + str(j[1]) + "\n Paitents saves " + str(dist[j[0]][3]))
